from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from owner.models import Owner
from owner.repository.owner_repository import OwnerRepository
from sale.repository.sale_repository import SaleRepository
from store.repository.store_repository import StoreRepository
from utils.request.req import is_method_post
from utils.request.required.required_field import required_field
from utils.serialize.cars.serialize_cars import serialize_by_sales


def call_create(name, email, call_back_success, call_back_error):
    try:
        if email and name:
            instance = Owner()
            instance.name = name
            instance.email = email
            instance.save()
            store = StoreRepository.create_or_get()
            store.owners.add(instance)
            return call_back_success('Proprietário salvo com sucesso!')

    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


def call_update(instance, name, email, call_back_success, call_back_error):
    try:
        if required_field(email) and required_field(name) and instance:
            instance.name = name
            instance.email = email
            instance.save()
            return call_back_success('Proprietário alterado com sucesso!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_owners.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_owners')

    if is_method_post(req):
        name = req.POST.get("name")
        email = req.POST.get("email")
        return call_create(name, email, call_back_success, call_back_error)

    return render(req, template_name)


@login_required(login_url='/')
def update(req, pk):
    instance_owner = get_object_or_404(Owner, pk=pk)
    template_name = 'update_owners.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_owners')

    if is_method_post(req):
        name = req.POST.get("name")
        email = req.POST.get("email")
        return call_update(instance_owner, name, email, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'cars': serialize_by_sales(SaleRepository.find_many_by_owner(instance_owner.id)),
            'instance': instance_owner
        }
    })


@login_required(login_url='/')
def delete(req, pk):
    instance_owner: Owner = get_object_or_404(Owner, pk=pk)

    if instance_owner.cars:
        if len(instance_owner.cars.all()) > 0:
            instance_owner.cars.clean()

    store = StoreRepository.create_or_get()

    if len(store.owners.all()) > 0:
        store.owners.remove(instance_owner)

    instance_owner.delete()

    messages.success(req, 'Proprietário removido com sucesso!')

    return redirect('list_owners')


@login_required(login_url='/')
def details(req, pk):
    instance_owner: Owner = get_object_or_404(Owner, pk=pk)
    template_name = 'details_owners.html'

    context = {
        'instance': instance_owner,
        'cars': serialize_by_sales(SaleRepository.find_many_by_owner(instance_owner.id)),
    }

    return render(req, template_name, {
        'context': context
    })


@login_required(login_url='/')
def list(req):
    template_name = 'list_owners.html'
    owners = OwnerRepository.find_all()

    context = {
        'owners': owners
    }

    return render(req, template_name, {
        'context': context
    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from owner.models import Owner
from owner.repository.owner_repository import OwnerRepository
from store.repository.store_repository import StoreRepository
from utils.request.req import is_method_post
from utils.request.required.required_field import required_field


def call_create(name, email, call_back_success, call_back_error):
    try:
        if email and name:
            instance = Owner()
            instance.name = name
            instance.email = email
            instance.save()
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
            return call_back_success('Proprietário salvo com sucesso!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_owners.html'

    def call_back_error(message):
        return render(req, template_name, {'context': {
            'message_error': message
        }})

    def call_back_success(message):
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
        return render(req, template_name, {'context': {
            'message_error': message
        }})

    def call_back_success(message):
        return redirect('list_owners')

    if is_method_post(req):
        name = req.POST.get("name")
        email = req.POST.get("email")
        return call_update(instance_owner, name, email, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'cars': instance_owner.cars.all(),
            'instance': instance_owner
        }
    })


@login_required(login_url='/')
def delete(req, pk):
    instance_owner: Owner = get_object_or_404(Owner, pk=pk)

    if instance_owner.cars:
        if len(instance_owner.cars.all()) > 0:
            instance_owner.cars.clean()

    store = StoreRepository.create_or_get('Carford')
    store.owners.delete(instance_owner)

    instance_owner.delete()

    return redirect('list_owners')


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

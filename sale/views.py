from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from car.repository.car_repository import CarRepository
from owner.models import Owner
from owner.repository.owner_repository import OwnerRepository
from sale.models import Sale
from sale.repository.sale_repository import SaleRepository
from store.repository.store_repository import StoreRepository
from utils.request.req import is_method_post
from utils.request.required.required_field import required_field


def call_create(price, owner, car, call_back_success, call_back_error):
    try:
        if required_field(price) and required_field(owner) and required_field(car):
            instance_owner: Owner = OwnerRepository.find_by_pk(owner)
            instance_car = CarRepository.find_pk(car)
            if len(SaleRepository.find_many_by_owner(instance_owner.id)) < 3:
                instance_owner.cars.add(instance_car)
                instance = Sale()
                instance.price = price
                instance.owner = instance_owner
                instance.car = instance_car
                instance.store = StoreRepository.create_or_get('Carford')
                instance.save()
                return call_back_success('Venda salva com sucesso!')

            return call_back_error(f'Proprietário {instance_owner.name} atingiu seu limite de carros')

    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


def call_update(instance, price, owner, car, call_back_success, call_back_error):
    try:
        if required_field(price) and required_field(owner) and required_field(car):
            instance.price = price
            instance.owner = OwnerRepository.find_by_pk(owner)
            instance.car = CarRepository.find_pk(car)
            instance.save()
            return call_back_success('Venda alterada com sucesso!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_sales.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_sales')

    if is_method_post(req):
        price = req.POST.get("price")
        car_id = req.POST.get("car")
        owner = req.POST.get("owner")
        return call_create(price, owner, car_id, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'cars': CarRepository.find_all(),
            'owners': OwnerRepository.find_all()
        }
    })


@login_required(login_url='/')
def update(req, pk):
    instance_sale = get_object_or_404(Sale, pk=pk)
    template_name = 'update_sales.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_sales')

    if is_method_post(req):
        price = req.POST.get("price")
        car_id = req.POST.get("car")
        owner = req.POST.get("owner")
        return call_update(instance_sale, price, owner, car_id, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'instance': instance_sale,
            'cars': CarRepository.find_all(),
            'owners': OwnerRepository.find_all(),
        }
    })


@login_required(login_url='/')
def delete(req, pk):
    instance_sale: Sale = get_object_or_404(Sale, pk=pk)

    instance_sale.delete()
    return redirect('list_sales')


@login_required(login_url='/')
def list(req):
    template_name = 'list_sales.html'
    sales = SaleRepository.find_by_all()

    context = {
        'sales': sales
    }

    return render(req, template_name, {
        'context': context
    })

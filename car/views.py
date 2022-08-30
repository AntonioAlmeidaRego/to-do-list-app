from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from car.models import Car
from car.repository.car_repository import CarRepository
from color.repository.color_repository import ColorRepository
from model_car.repository.model_repository import ModelCarRepository
from owner.repository.owner_repository import OwnerRepository
from store.repository.store_repository import StoreRepository
from utils.request.req import is_method_post


def call_create(name, color, model, call_back_success, call_back_error):
    try:
        if color and name and model:
            instance_color = ColorRepository.find_by_pk(color)
            instance_model = ModelCarRepository.find_by_pk(model)
            if instance_color and instance_model:
                instance = Car()
                instance.model = instance_model
                instance.color = instance_color
                instance.name = name
                instance.save()
                store = StoreRepository.create_or_get()
                store.cars.add(instance)
                return call_back_success('Carro salvo com sucesso!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


def call_update(instance, name, color, model, call_back_success, call_back_error):
    try:
        if color and name and model:
            instance_color = ColorRepository.find_by_pk(color)
            instance_model = ModelCarRepository.find_by_pk(model)
            if instance_color and instance_model:
                instance.model = instance_model
                instance.color = instance_color
                instance.name = name
                instance.save()
                return call_back_success('Carro Alterado com sucesso!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Informe os dados corretamente!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_car.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_cars')

    if is_method_post(req):
        name = req.POST.get("name")
        color = req.POST.get("color")
        model = req.POST.get("model")
        return call_create(name, color, model, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'colors': ColorRepository.find_all(),
            'models': ModelCarRepository.find_all(),
        }
    })


@login_required(login_url='/')
def update(req, pk):
    instance_car = get_object_or_404(Car, pk=pk)
    template_name = 'update_car.html'

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_cars')

    if is_method_post(req):
        name = req.POST.get("name")
        color = req.POST.get("color")
        model = req.POST.get("model")
        return call_update(instance_car, name, color, model, call_back_success, call_back_error)

    return render(req, template_name, {
        'context': {
            'colors': ColorRepository.find_all(),
            'models': ModelCarRepository.find_all(),
            'instance': instance_car
        }
    })


@login_required(login_url='/')
def delete(req, pk):
    instance_car = get_object_or_404(Car, pk=pk)

    store = StoreRepository.create_or_get()

    owner = OwnerRepository.find_by_car(instance_car)

    if store:
        if len(store.cars.all()) > 0:
            store.cars.remove(instance_car)

    if owner:
        owner.cars.remove(instance_car)
    instance_car.delete()

    messages.success(request=req, message='Carro removido com sucesso!')

    return redirect('list_cars')


@login_required(login_url='/')
def list(req):
    template_name = 'list_cars.html'
    cars = CarRepository.find_all()

    context = {
        'cars': cars
    }

    return render(req, template_name, {
        'context': context
    })

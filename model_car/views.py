from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from model_car.models import ModelCar
from model_car.repository.model_repository import ModelCarRepository
from utils.request.req import is_method_post


def call_create(type_color, call_back_success, call_back_error):
    try:
        type_color = int(type_color)
        if 1 <= type_color < 4:
            instance_db = ModelCarRepository.find_by_type(type_color)
            if not instance_db:
                instance = ModelCar()
                instance.type_model = type_color
                instance.save()
                return call_back_success('Modelo salvo com sucesso!')
            return call_back_error('Modelo já salvo, tente outro!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Escolha um modelo válida!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_model.html'
    type_model = req.POST.get("model")

    context = {}

    def call_back_error(message):
        messages.error(req, message)
        return render(req, template_name)

    def call_back_success(message):
        messages.success(req, message)
        return redirect('list_models')

    if is_method_post(req):
        return call_create(type_model, call_back_success, call_back_error)

    return render(req, template_name, context)


@login_required(login_url='/')
def list(req):
    template_name = 'list_model.html'
    colors = ModelCarRepository.find_all()

    context = {
        'models': colors
    }

    return render(req, template_name, {
        'context': context
    })

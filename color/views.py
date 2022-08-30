from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from color.models import Color
from color.repository.color_repository import ColorRepository
from utils.request.req import is_method_post


def call_create(type_color, call_back_success, call_back_error):
    try:
        type_color = int(type_color)
        print(type_color)
        if 1 <= type_color < 4:
            instance_db = ColorRepository.find_by_type(type_color)
            print(instance_db)
            if not instance_db:
                instance = Color()
                instance.type_color = type_color
                instance.save()
                return call_back_success('Cor salva com sucesso!')
            return call_back_error('Cor já salvo, tente outro!')
    except Exception as e:
        print("error: ", e)
        ...
    return call_back_error('Escolha uma cor válida!')


@login_required(login_url='/')
def create(req):
    template_name = 'create_color.html'
    type_color = req.POST.get("color")

    context = {}

    def call_back_error(message):
        return render(req, template_name, {'context': {
            'message_error': message
        }})

    def call_back_success(message):
        return redirect('list_colors')

    if is_method_post(req):
        return call_create(type_color, call_back_success, call_back_error)

    return render(req, template_name, context)


@login_required(login_url='/')
def list(req):
    template_name = 'list_color.html'
    colors = ColorRepository.find_all()

    context = {
        'colors': colors
    }

    return render(req, template_name, {
        'context': context
    })

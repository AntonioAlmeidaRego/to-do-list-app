from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from utils.authentication.authentication import auth
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login


def login(req):
    template_name = 'login.html'
    if req.method == 'POST':
        email = req.POST.get("email")
        password = req.POST.get("password")

        def call_back_success(user):
            auth_login(req, user)
            return redirect('dashboard')

        def call_back_error(message):
            return render(req, template_name, {'context': {
                'message_error': message
            }})

        return auth(email=email, password=password, call_back_success=call_back_success,
                    call_back_error=call_back_error)

    return render(req, template_name)


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/')
def dashboard(req):
    template_name = 'dashboard.html'
    return render(req, template_name)

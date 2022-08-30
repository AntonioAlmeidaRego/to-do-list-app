from django.contrib.auth import (
    authenticate,
)

from person.models import Person


def auth(email=None, password=None, call_back_success=None, call_back_error=None):
    message_required = "Preencha os campos abaixo"
    if email and password:
        message_error = "Usuário Inválido"
        if call_back_success:
            try:
                user = Person.objects.get(username=email)

                if not user:
                    return call_back_error(message_error)

                if not user.check_password(password):
                    return call_back_error(message_error)

                user = authenticate(username=email, password=password)
                return call_back_success(user)

            except Exception:
                return call_back_error(message_error)
    return call_back_error(message_required)

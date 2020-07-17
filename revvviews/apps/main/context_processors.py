from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import RegistrationForm


def auth_forms(request):
    return {
        'login_form': AuthenticationForm(),
        'register_form': RegistrationForm(),
    }

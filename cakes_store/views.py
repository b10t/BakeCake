import string
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from cakes_store.models import User
from django.core.mail import EmailMessage
from cakes_store.forms import UserCreationForm
from django.http import HttpResponse


def index(request):
    context = {
        'Step': 'Number'
    }
    return render(request, 'index.html', context)


def reg(request):
    context = {
        'Step': 'Number',
    }

    if request.method == 'POST':
        email = request.POST['REG']
        password = get_random_password()

        User.objects._create_user(
            password=password,
            email=request.POST['REG'],
            username=request.POST['REG'],
        )
        subject_message = 'CakeBake'
        message = f'Ваш пароль: {password}'
        EmailMessage(
            subject=subject_message,
            body=message,
            to=[request.POST['REG']],
            ).send()
        return render(request, 'index.html', context)


def get_random_password():
    password_len = 8
    allowed_chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = get_random_string(password_len, allowed_chars=allowed_chars)
    return password


    if request.method == 'POST':
        return render(request, 'index.html', context)
        # form = RegisterUserForm_fiz(request.POST)
        # if form.is_valid():
        #     contract = form.save()
        #     return render(request, 'registration/register_ok.html')
        # else:
        #     return render(request, 'registration/register_fiz.html', {'form': form})
    else:
        return render(request, 'index.html', context)

        # form = RegisterUserForm_fiz()
        # return render(request, 'registration/register_fiz.html', {'form': form})
    # return render(request, 'main/uconstruction.html')

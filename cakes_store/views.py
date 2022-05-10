import re
import string
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from cakes_store.models import User, Customer
from django.core.mail import EmailMessage



def index(request):
    context = {}
    return render(request, 'index.html', context)

def lk(request):
    context = {}
    return render(request, 'lk.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def get_random_password():
    password_len = 8
    allowed_chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = get_random_string(password_len, allowed_chars=allowed_chars)
    return password


def signup(request):
    context = {}
    try:
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
            return redirect('login')
        if request.method == 'GET':
            return render(request, 'signup.html', context)
    except Exception as error:
        context = {'error': error}
        return render(request, 'signup.html', context)


def processing_orders(request):
    """Обработка заказа"""
    if request.method == 'POST':
        context = {}
        return render(request, 'index.html', context)

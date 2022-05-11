import re
import string

from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
# from turtle import fd
from django.utils.crypto import get_random_string

from cakes_store.models import (Cake, Customer, Order, User, save_cake,
                                save_order)


def index(request):
    context = {}
    return render(request, 'index.html', context)


def lk(request):
    context = {}
    user = request.user
    try:
        if user.is_authenticated:
            order = Order.objects.get(customer=user.order_customer)
            context = {
                'order': order,
            }
        return render(request, 'lk.html', context)
    except Exception:
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
                email=email,
                username=email,
            )
            subject_message = 'CakeBake'
            message = f'Ваш пароль: {password}'
            EmailMessage(
                subject=subject_message,
                body=message,
                to=[email],
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

        # new_cake = save_cake(
        #     levels=Cake.CAKE_LEVELS[int(request.POST["LEVELS"]) - 1][0],
        #     shape=Cake.CAKE_SHAPES[int(request.POST["FORM"]) - 1][0],
        #     toppings=Cake.CAKE_TOPPINGS[int(request.POST["TOPPING"]) - 1][0],
        #     berries=Cake.BERRIES[int(request.POST["BERRIES"]) - 1][0],
        #     decor=Cake.CAKE_DECORS[int(request.POST["DECOR"]) - 1][0],
        #     title=request.POST["WORDS"],
        #     price=123.45
        # )
        # try:
        #     customer = Customer.objects.get(email=request.POST["EMAIL"])
        # except Exception:
        #     customer = Customer(
        #         customer=User.objects.get(email='system@bakecake.ru'),
        #         customer_name='temporary',
        #         customer_email=request.POST["EMAIL"],
        #         customer_phone=request.POST["PHONE"]
        #     )
        #     customer.save()

        # new_order = save_order(
        #     cake=new_cake,
        #     customer=customer,
        #     address=request.POST["ADDRESS"],
        #     delivery_date=request.POST["DATE"],
        #     delivery_time=request.POST["TIME"],
        #     comment=request.POST["COMMENTS"]
        # )
        return render(request, 'index.html', context)

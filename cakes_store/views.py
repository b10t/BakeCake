from email.policy import default
import string

from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

from cakes_store.models import (Cake, Order, User)


def get_random_password(password_len=8):
    """Генерирует случайный пароль."""
    allowed_chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = get_random_string(password_len, allowed_chars=allowed_chars)
    return password


def save_order_to_session(request):
    """Сохраняет параметры торта в сессию."""
    order = request.POST.dict()

    del order['csrfmiddlewaretoken']
    order = dict((k.lower(), v) for k, v in order.items())

    request.session['order'] = order


def create_order(request):
    """Создание заказа."""
    user = request.user
    order_context = request.session['order']

    cake = Cake()
    cake.berries = order_context.get('berries', '0')
    cake.decor = order_context.get('decor', '0')
    cake.words = order_context.get('words')
    cake.levels = order_context.get('levels')
    cake.topping = order_context.get('topping')
    cake.price = float(order_context.get('price'))
    cake.form = order_context.get('form')
    cake.save()

    order = Order()
    order.customer = user
    order.cake = cake
    order.customer_name = order_context.get('name')
    order.customer_email = order_context.get('email')
    order.order_address = order_context.get('address')
    order.delivery_date = order_context.get('date')
    order.delivery_time = order_context.get('time')
    order.comment = order_context.get('comments')
    order.save()

    del request.session['order']


def index(request):
    context = {}
    return render(request, 'index.html', context)


def lk(request):
    context = {}
    user = request.user
    try:
        if user.is_authenticated:
            orders = user.order_customer.all()
            context = {
                'orders': orders,
            }
        return render(request, 'lk.html', context)
    except Exception as error:
        context = {'error': error}
        return render(request, 'lk.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


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
    user = request.user

    if request.method == 'POST':
        context = {}

        post = request.POST

        save_order_to_session(request)

        if user.is_authenticated:
            create_order(request)

            return redirect('lk')
        else:
            email = post["EMAIL"]

            if User.objects.filter(email=email).exists():
                # Отправляем на вход
                pass
            else:
                # Отправляем на регистрацию
                return redirect('login')

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

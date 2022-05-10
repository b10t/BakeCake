from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomManager(BaseUserManager):

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Должна быть электронная почта')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(verbose_name='имя', max_length=150)

    is_staff = models.BooleanField(_('staff status'), default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True)
    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Cake(models.Model):
    CAKE_TOPPINGS = (
        ('Without', 'Без топпинга'),
        ('White sauce', 'Белый соус'),
        ('Caramel', 'Карамельный'),
        ('Maple', 'Кленовый'),
        ('Blueberry', 'Черничный'),
        ('Milk chocolate', 'Молочный шоколад'),
        ('Strawberry', 'Клубничный'),
    )
    CAKE_LEVELS = (
        ('1', '1 уровень'),
        ('2', '2 уровня'),
        ('3', '3 уровня'),
    )
    CAKE_SHAPES = (
        ('circle', 'Круг'),
        ('square', 'Квадрат'),
        ('rectangle', 'Прямоугольник'),
    )
    CAKE_DECORS = (
        ('Pistachios', 'Фисташки'),
        ('Meringue', 'Безе'),
        ('Hazelnuts', 'Фундук'),
        ('Pecan', 'Пекан'),
        ('Marshmallow', 'Маршмеллоу'),
        ('Marzipan', 'Марципан'),
    )
    BERRIES = (
        ('Blackberry', 'Ежевика'),
        ('Raspberry', 'Малина'),
        ('Blueberry', 'Голубика'),
        ('Strawberry', 'Клубника'),
    )
    berries = models.CharField(
        'Ягоды', choices=BERRIES, max_length=20,
    )
    decor = models.CharField(
        'Декор', choices=CAKE_DECORS, max_length=20,
    )
    title = models.CharField('Надпись', max_length=200, blank=True)

    levels = models.CharField(
        'Уровни', choices=CAKE_LEVELS, max_length=20,
    )
    toppings = models.CharField(
        'Топпинг', choices=CAKE_TOPPINGS, max_length=20,
    )
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    shape = models.CharField('Форма', choices=CAKE_SHAPES, max_length=20, default='Circle')

    def __str__(self):
        return f'{self.title}, {self.berries}, {self.decor}, {self.levels}, {self.toppings}, {self.shape}'

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


def save_cake(levels, shape, toppings, berries, decor, title, price):
    new_cake = Cake(
        levels=levels,
        shape=shape,
        toppings=toppings,
        berries=berries,
        decor=decor,
        title=title,
        price=price
    )
    new_cake.save()
    return new_cake


class Order(models.Model):
    customer = models.OneToOneField(
        'Customer', verbose_name='Покупатель', on_delete=models.DO_NOTHING, null=True, related_name='customer_cake'
    )
    cake = models.OneToOneField(
        Cake, verbose_name='Торт', on_delete=models.CASCADE, related_name='order_cake'
    )
    order_address = models.CharField('Адрес', max_length=250)
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.TimeField('Время доставки')
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return self.customer.customer_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Customer(models.Model):
    customer = models.OneToOneField(
        User, verbose_name='Заказчик', on_delete=models.DO_NOTHING, related_name='order_customer'
    )
    customer_name = models.CharField('Имя', max_length=60)
    customer_email = models.EmailField('Электронная почта', max_length=254)
    customer_phone = PhoneNumberField(verbose_name='Номер телефона', region='RU')

    def __str__(self):
        return self.customer_name



def save_order(cake, customer, phone, address, delivery_date, delivery_time, comment):
    new_order = Order(
        cake=cake,
        customer=customer,
        customer_phone=phone,
        customer_address=address,
        delivery_date=delivery_date,
        delivery_time=delivery_time,
        comment=comment
    )
    new_order.save()
    return new_order

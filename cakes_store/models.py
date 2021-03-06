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
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return f'{self.username}, {self.email if self.email else "no email"}'

    def get_full_name(self):
        return f'{self.username}, {self.email if self.email else "no email"}'

    def get_short_name(self):
        return self.username


class Cake(models.Model):
    CAKE_TOPPINGS = (
        ('1', 'Без топпинга'),
        ('2', 'Белый соус'),
        ('3', 'Карамельный'),
        ('4', 'Кленовый'),
        ('5', 'Черничный'),
        ('6', 'Молочный шоколад'),
        ('7', 'Клубничный'),
    )
    CAKE_LEVELS = (
        ('1', '1 уровень'),
        ('2', '2 уровня'),
        ('3', '3 уровня'),
    )
    CAKE_SHAPES = (
        ('1', 'Круг'),
        ('2', 'Квадрат'),
        ('3', 'Прямоугольник'),
    )
    CAKE_DECORS = (
        ('0', 'Нет'),
        ('1', 'Фисташки'),
        ('2', 'Безе'),
        ('3', 'Фундук'),
        ('4', 'Пекан'),
        ('5', 'Маршмеллоу'),
        ('6', 'Марципан'),
    )
    BERRIES = (
        ('0', 'Нет'),
        ('1', 'Ежевика'),
        ('2', 'Малина'),
        ('3', 'Голубика'),
        ('4', 'Клубника'),
    )
    berries = models.CharField(
        'Ягоды', choices=BERRIES, max_length=1, default='0'
    )
    decor = models.CharField(
        'Декор', choices=CAKE_DECORS, max_length=1, default='0'
    )
    words = models.CharField(
        'Надпись', max_length=200, blank=True
    )
    levels = models.CharField(
        'Уровни', choices=CAKE_LEVELS, max_length=1,
    )
    topping = models.CharField(
        'Топпинг', choices=CAKE_TOPPINGS, max_length=1,
    )
    price = models.DecimalField(
        'Цена', max_digits=8, decimal_places=2
    )
    form = models.CharField(
        'Форма', choices=CAKE_SHAPES, max_length=1,
    )

    def __str__(self):
        return f'Торт # {self.words}, \
                {self.get_berries_display()}, \
                {self.get_decor_display()}, \
                {self.get_levels_display()}, \
                {self.get_topping_display()}, \
                {self.get_form_display()}'

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


class Order(models.Model):
    customer = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.CASCADE, null=True, related_name='order_customer'
    )
    cake = models.OneToOneField(
        Cake, verbose_name='Торт', on_delete=models.CASCADE, related_name='order_cake'
    )
    customer_name = models.CharField(
        'Имя', max_length=60, default=''
    )
    customer_email = models.EmailField(
        'Электронная почта',
        max_length=254,
        default=''
    )
    order_address = models.CharField('Адрес', max_length=250)
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.TimeField('Время доставки')
    comment = models.TextField('Комментарий', blank=True)
    promo = models.CharField('Промо код', max_length=12, blank=True, null=True)

    def __str__(self):
        return f'Покупатель: {self.customer.username}. Торт: "{self.cake}"'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

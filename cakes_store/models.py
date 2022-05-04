from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


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
        'Ягоды', choices=BERRIES, blank=True, max_length=20,
    )
    decor = models.CharField(
        'Декор', choices=CAKE_DECORS, blank=True, max_length=20,
    )
    title = models.CharField('Надпись', max_length=200, blank=True)

    levels = models.CharField(
        'Уровни', choices=CAKE_LEVELS, max_length=20,
    )
    toppings = models.CharField(
        'Топпинг', choices=CAKE_TOPPINGS, max_length=20,
    )
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


class Order(models.Model):
    customer = models.ForeignKey(
        User, verbose_name='Заказчик', on_delete=models.DO_NOTHING,
    )
    cake = models.ForeignKey(
        Cake, verbose_name='Торт', on_delete=models.CASCADE,
    )
    customer_name = models.CharField('Имя', max_length=60)
    customer_email = models.EmailField('Электронная почта', max_length=254)
    customer_phone = PhoneNumberField(
        verbose_name='Номер телефона', region='RU'
    )
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.TimeField('Время доставки')
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

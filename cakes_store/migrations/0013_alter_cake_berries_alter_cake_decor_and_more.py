# Generated by Django 4.0.4 on 2022-05-11 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakes_store', '0012_merge_20220511_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='berries',
            field=models.CharField(choices=[('0', 'Нет'), ('1', 'Ежевика'), ('2', 'Малина'), ('3', 'Голубика'), ('4', 'Клубника')], default='0', max_length=1, verbose_name='Ягоды'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='decor',
            field=models.CharField(choices=[('0', 'Нет'), ('1', 'Фисташки'), ('2', 'Безе'), ('3', 'Фундук'), ('4', 'Пекан'), ('5', 'Маршмеллоу'), ('6', 'Марципан')], default='0', max_length=1, verbose_name='Декор'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='levels',
            field=models.CharField(choices=[('1', '1 уровень'), ('2', '2 уровня'), ('3', '3 уровня')], max_length=1, verbose_name='Уровни'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='shape',
            field=models.CharField(choices=[('1', 'Круг'), ('2', 'Квадрат'), ('3', 'Прямоугольник')], max_length=1, verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='toppings',
            field=models.CharField(choices=[('1', 'Без топпинга'), ('2', 'Белый соус'), ('3', 'Карамельный'), ('4', 'Кленовый'), ('5', 'Черничный'), ('6', 'Молочный шоколад'), ('7', 'Клубничный')], max_length=1, verbose_name='Топпинг'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_customer', to='cakes_store.customer', verbose_name='Покупатель'),
        ),
    ]
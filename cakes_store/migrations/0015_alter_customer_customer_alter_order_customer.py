# Generated by Django 4.0.4 on 2022-05-11 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakes_store', '0014_rename_shape_cake_form_rename_toppings_cake_topping_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='cakes_store.customer', verbose_name='Покупатель'),
        ),
    ]
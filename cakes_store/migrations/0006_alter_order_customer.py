# Generated by Django 4.0.4 on 2022-05-10 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakes_store', '0005_remove_customer_order_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_cake', to='cakes_store.customer', verbose_name='Покупатель'),
        ),
    ]

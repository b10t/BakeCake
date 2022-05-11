# Generated by Django 4.0.4 on 2022-05-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes_store', '0017_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(default='', max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='', max_length=60, verbose_name='Имя'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-11 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes_store', '0013_alter_cake_berries_alter_cake_decor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='shape',
            new_name='form',
        ),
        migrations.RenameField(
            model_name='cake',
            old_name='toppings',
            new_name='topping',
        ),
        migrations.RenameField(
            model_name='cake',
            old_name='title',
            new_name='words',
        ),
    ]
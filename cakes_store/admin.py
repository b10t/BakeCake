from django.contrib import admin

from cakes_store.models import Cake, Order, User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from cakes_store.forms import UserCreationForm


@admin.register(User)
class UserAdminConfig(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_admin', 'is_active')
    search_fields = ('username', 'email', 'is_active')
    list_filter = ('is_staff', 'is_admin', 'is_active')


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cake',)


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('customer_name',)

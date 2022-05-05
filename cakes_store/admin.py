from django.contrib import admin

from cakes_store.models import Cake, Order
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from cakes_store.forms import UserCreationForm

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )
    add_form = UserCreationForm


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', )

from django.contrib import admin

from cakes_store.models import Cake, Order


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', )

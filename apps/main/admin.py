from django.contrib import admin
from .models import Menu, Item
from .translations import CustomTranslationsAdmin


@admin.register(Menu)
class MenuAdmin(CustomTranslationsAdmin):
    list_display = ['name']


@admin.register(Item)
class ItemAdmin(CustomTranslationsAdmin):
    list_filter = ['menu']
    list_display = ['name', 'menu']

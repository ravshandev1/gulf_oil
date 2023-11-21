from django.contrib import admin
from .models import Menu, Item, Country, Contact, ContactPublic
from .translations import CustomAdmin, InlineAdmin


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    inlines = [ContactInline]


@admin.register(ContactPublic)
class ContactPublicAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email']


class ItemInline(InlineAdmin):
    model = Item
    extra = 0


@admin.register(Menu)
class MenuAdmin(CustomAdmin):
    list_display = ['name']
    inlines = [ItemInline]

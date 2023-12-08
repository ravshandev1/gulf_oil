from django.contrib import admin
from .models import Menu, Item, Contact, ContactPublic, Advertising
from .translations import CustomAdmin, InlineAdmin


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['staff', 'phone']
    filter_horizontal = ['country']
    exclude = ['country_count']


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

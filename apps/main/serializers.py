from rest_framework import serializers
from .models import Menu, Item, ContactPublic, Contact


class ContactPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPublic
        fields = ['address', 'email', 'website', 'phone']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['address', 'email', 'staff', 'phone']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'image']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']


class ItemPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['pdf']

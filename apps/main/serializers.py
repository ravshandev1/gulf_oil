from rest_framework import serializers
from .models import Menu, Item, ContactPublic, Contact
from django.conf import settings


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

    image = serializers.SerializerMethodField()

    @staticmethod
    def get_image(obj):
        return f"{settings.BASE_URL}{obj.image.url}"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['pdf']

    pdf = serializers.SerializerMethodField()

    @staticmethod
    def get_pdf(obj):
        return f"{settings.BASE_URL}{obj.pdf.url}"


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'image']

    image = serializers.SerializerMethodField()

    @staticmethod
    def get_image(obj):
        return f"{settings.BASE_URL}{obj.image.url}"

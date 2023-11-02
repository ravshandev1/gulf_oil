from rest_framework import serializers
from .models import Menu, Item


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'image', 'items_count']

    items_count = serializers.SerializerMethodField()

    @staticmethod
    def get_items_count(obj):
        return obj.items.count()


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description']

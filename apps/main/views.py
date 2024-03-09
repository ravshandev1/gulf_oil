import jwt
from django.conf import settings
from rest_framework import generics, response
from .models import Menu, Item, ContactPublic, Contact, Advertising
from .serializers import MenuSerializer, ItemSerializer, PDFSerializer, ContactSerializer, ContactPublicSerializer, \
    AdvertisingSerializer


class AdvertisingAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        qs = Advertising.objects.all()
        data = list()
        for item in qs:
            data.append(jwt.encode(AdvertisingSerializer(item).data, settings.SECRET_KEY, settings.ALGORITIHM))
        return response.Response(data)


class ContactPublicAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        qs = ContactPublic.objects.all()
        data = list()
        for item in qs:
            data.append(jwt.encode(ContactPublicSerializer(item).data, settings.SECRET_KEY, settings.ALGORITIHM))
        return response.Response(data)


class ContactAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        qs = Contact.objects.filter(country__code__exact=self.request.query_params.get('code'))
        data = list()
        for item in qs:
            data.append(jwt.encode(ContactSerializer(item).data, settings.SECRET_KEY, settings.ALGORITIHM))
        return response.Response(data)


class MenuAPI(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        qs = Menu.objects.all()
        data = list()
        for item in qs:
            data.append(jwt.encode(MenuSerializer(item).data, settings.SECRET_KEY, settings.ALGORITIHM))
        return response.Response(data)


class ItemAPI(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        name = self.request.query_params.get('name')
        if name:
            qs = Item.objects.filter(menu_id=self.kwargs.get('pk'), name__icontains=name)
        else:
            qs = Item.objects.filter(menu_id=self.kwargs.get('pk'))
        data = list()
        for item in qs:
            data.append(jwt.encode(ItemSerializer(item).data, settings.SECRET_KEY, settings.ALGORITIHM))
        return response.Response(data)


class ItemPDFAPI(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = PDFSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = jwt.encode(serializer.data, settings.SECRET_KEY, settings.ALGORITIHM)
        return response.Response(data)

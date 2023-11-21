from rest_framework import generics
from .models import Menu, Item, ContactPublic, Contact, Country
from .serializers import MenuSerializer, ItemSerializer, ItemPDFSerializer, ContactSerializer, ContactPublicSerializer


class ContactPublicAPI(generics.ListAPIView):
    queryset = ContactPublic.objects.all()
    serializer_class = ContactPublicSerializer


class ContactAPI(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        country = Country.objects.filter(code__exact=self.request.query_params.get('code')).first()
        return Contact.objects.filter(country=country)


class MenuAPI(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemAPI(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            return Item.objects.filter(menu_id=self.kwargs.get('pk'), name__exact=name)
        return Item.objects.filter(menu_id=self.kwargs.get('pk'))


class ItemPDFAPI(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemPDFSerializer

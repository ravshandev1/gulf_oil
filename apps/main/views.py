from rest_framework import generics
from .models import Menu, Item, ContactPublic, Contact, Advertising
from .serializers import MenuSerializer, ItemSerializer, PDFSerializer, ContactSerializer, ContactPublicSerializer, \
    AdvertisingSerializer


class AdvertisingAPI(generics.ListAPIView):
    serializer_class = AdvertisingSerializer
    queryset = Advertising.objects.all()


class ContactPublicAPI(generics.ListAPIView):
    serializer_class = ContactPublicSerializer
    queryset = ContactPublic.objects.all()


class ContactAPI(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(country__code__exact=self.request.query_params.get('code'))


class MenuAPI(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class ItemAPI(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            return Item.objects.filter(menu_id=self.kwargs.get('pk'), name__icontains=name)
        return Item.objects.filter(menu_id=self.kwargs.get('pk'))


class ItemPDFAPI(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = PDFSerializer

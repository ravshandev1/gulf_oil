from rest_framework import generics, views, response
from .models import Menu, Item
from .serializers import MenuSerializer, ItemSerializer


class MenuAPI(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = Item.objects.filter(menu_id=self.kwargs.get('pk'))
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__icontains=name)
        serializer = ItemSerializer(qs, many=True)
        return response.Response(serializer.data)


class ItemRetrieveAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = Item.objects.filter(id=self.kwargs.get('pk')).first()
        return response.Response({'pdf': f"https://gulf.ravshandev.uz{obj.pdf.url}"})

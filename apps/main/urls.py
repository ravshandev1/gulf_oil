from django.urls import path
from .views import MenuAPI, ItemAPI, ItemPDFAPI, ContactAPI, ContactPublicAPI, AdvertisingAPI

urlpatterns = [
    path('', MenuAPI.as_view()),
    path('<int:pk>/', ItemAPI.as_view()),
    path('item/<int:pk>/', ItemPDFAPI.as_view()),
    path('contact-public/', ContactPublicAPI.as_view()),
    path('contact/', ContactAPI.as_view()),
    path('advertising/', AdvertisingAPI.as_view()),
]

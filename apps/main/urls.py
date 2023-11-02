from django.urls import path
from .views import MenuAPI, ItemAPI, ItemRetrieveAPI

urlpatterns = [
    path('', MenuAPI.as_view()),
    path('<int:pk>/', ItemAPI.as_view()),
    path('item/<int:pk>/', ItemRetrieveAPI.as_view()),
]

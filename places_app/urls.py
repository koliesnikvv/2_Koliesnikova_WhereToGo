from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.places_list, name='places_list'),
    path('places/add/', views.add_place, name='add_place'),
    path('places/<int:pk>/', views.place_detail, name='place_detail'),
]
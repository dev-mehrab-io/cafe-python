from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.drinks_list, name='drinks_list'),
    path('drinks/add/', views.add_drink),
    path('drinks/<int:id>/', views.drink_detail)
]
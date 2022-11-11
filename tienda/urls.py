from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('listadoProductos/', views.listadoProductos, name='listadoProductos'),
    path('tienda/', views.welcome, name='welcome'),
]

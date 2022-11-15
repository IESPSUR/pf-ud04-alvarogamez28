from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('listadoProductos/', views.listadoProductos, name='listadoProductos'),
    path('tienda/', views.welcome, name='welcome'),
    path('producto/nuevo/', views.nuevoProducto, name='nuevoProducto'),
    path('producto/<str:pk>',views.eliminarProducto, name='eliminarProducto'),
    path('producto/editar/<str:pk>', views.editarProducto, name='editarProducto'),
]

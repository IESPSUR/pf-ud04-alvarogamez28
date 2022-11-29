from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('listadoProductos/', views.listadoProductos, name='listadoProductos'),
    path('producto/nuevo/', views.nuevoProducto, name='nuevoProducto'),
    path('producto/<str:pk>',views.eliminarProducto, name='eliminarProducto'),
    path('producto/editar/<str:pk>', views.editarProducto, name='editarProducto'),
    path('compraProductos/', views.compraProductos, name='compraProductos'),
    path('producto/comprar/<str:pk>', views.productoCompra, name='productoCompra'),
    path('producto/comprar/checkout/<str:pk>', views.checkout, name='checkout'),
    path('informes/', views.informes, name='informes'),
    path('Informes/Marcas/', views.marca, name='marca'),
    path('Informes/Marcas/Productos/<str:nombremarca>', views.productos_in_marca, name='productos_in_marca'),
]

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Compra , Producto, Marca

admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Marca)
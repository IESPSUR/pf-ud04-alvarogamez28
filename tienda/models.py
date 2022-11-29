from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Marca(models.Model):
    nombreMarca = models.TextField()
    def __str__(self):
        return self.nombreMarca
class Producto(models.Model):
    nombreProducto = models.TextField(primary_key=True)
    modelo = models.TextField()
    unidadesProducto = models.IntegerField()
    precio = models.IntegerField()
    detalles = models.TextField()
    marca = models.ForeignKey(Marca, models.PROTECT)

    def __str__(self):
        return self.nombreProducto

class Compra(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    importe = models.IntegerField()
    unidadesCompra = models.IntegerField()
    producto = models.ForeignKey(Producto, models.PROTECT)

    def __str__(self):
        return self.producto.nombreProducto
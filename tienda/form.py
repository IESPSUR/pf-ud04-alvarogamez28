from django import forms

from .models import Producto

class PostForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombreProducto', 'modelo', 'unidadesProducto', 'precio', 'detalles', 'marca',)
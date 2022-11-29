import calculation
from django import forms

from .models import Producto, Compra

class PostForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class CompraForm(forms.ModelForm):
    precio = forms.DecimalField(disabled=True)
    unidadesProducto = forms.DecimalField()
    importe = forms.DecimalField(widget=calculation.FormulaInput('unidadesProducto*precio'))
    class Meta:
        model = Compra
        model = Producto
        fields = ('precio',)
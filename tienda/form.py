from django import forms

from .models import Producto

class PostForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class CheckOutForm(forms.Form):
    unidades = forms.FloatField(label='unidades')
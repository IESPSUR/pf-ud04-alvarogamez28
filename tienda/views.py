from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listadoProductos(request):

    return render(request,'tienda/listadoProductos.html', {})

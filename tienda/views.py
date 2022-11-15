from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .form import PostForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})



def listadoProductos(request):
    productos = Producto.objects.filter().order_by('nombreProducto')
    return render(request,'tienda/listadoProductos.html', {'productos': productos})


def nuevoProducto(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombreProducto')
            return render(request, 'tienda/listadoProductos.html', {'productos': productos})
    else:
        form = PostForm()
    return render(request, 'tienda/producto_nuevo.html', {'form': form})

def eliminarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    productos = Producto.objects.filter().order_by('nombreProducto')
    return render(request, 'tienda/listadoProductos.html', {'productos': productos})

def editarProducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombreProducto')
            return render(request, 'tienda/listadoProductos.html', {'productos': productos})
    else:
        form = PostForm(instance=producto)
    return render(request, 'tienda/nuevoProducto.html', {'form': form})
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Compra, Marca
from .form import PostForm, CompraForm


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
    return render(request, 'tienda/nuevoProducto.html', {'form': form})

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


def compraProductos(request):
    productos = Producto.objects.filter().order_by('nombreProducto')
    return render(request, 'tienda/compraProductos.html', {'productos': productos})

def productoCompra(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=producto)
        if form.is_valid():
            unidades = form.cleaned_data['unidadesProducto']
            importe = form.cleaned_data['importe']

            if producto.unidadesProducto < unidades :
                return redirect('productoCompra',pk)
            else:
                Compra.objects.create(fecha=timezone.now(), importe=importe, unidadesCompra=unidades, producto=producto)
                producto.unidadesProducto = producto.unidadesProducto-unidades
                producto.save();
                return redirect('checkout', pk);

    else:
        form = CompraForm(instance=producto)
    return render(request, 'tienda/productoCompra.html', {'form': form})

def checkout(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/checkout.html', {'producto':producto})
def informes(request):
        return render(request, 'tienda/informes.html')

def marca(request):
    marca = Marca.objects.filter().order_by('nombreMarca')
    return render(request, 'tienda/marca.html', {'marca': marca})

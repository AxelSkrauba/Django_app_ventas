from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Gestion.models import Clientes, Articulos, Relaciones
from .forms import ClienteForm, ArticuloForm, VentaForm
from django.utils import timezone

def principal(request):
    return render(request, "principal.html")

def default(request):
    return render(request, "default.html")

def clientes(request):
    clientes = Clientes.objects.all()
    return render(request, "clientes.html", {'clientes':clientes})

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #Elegir retorno, mostrar que se agrego correctamente el cliente por ejemplo...
            return clientes(request)
    else:
        form = ClienteForm()

    return render(request, 'cliente_new.html', {'form': form})

#Para modificacion de datos de cliente
def cliente_edit(request, id_cliente):
    #pk = primary key, identificador en DB

    post = get_object_or_404(Clientes, pk=id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #Elegir retorno, mostrar que se modifico correctamente el cliente por ejemplo...
            return clientes(request)
    else:
        form = ClienteForm(instance=post)
    return render(request, 'cliente_edit.html', {'form': form, 'id_cliente':id_cliente})

def cliente_delete(request, id_cliente):
    #Ver si hace falta confirmacion o algo...
    post = get_object_or_404(Clientes, pk=id_cliente)
    post.delete()          
    return clientes(request)

def ventas(request):
    ventas = Relaciones.objects.all()
    return render(request, "ventas.html", {'ventas':ventas})

def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha = timezone.now() #from django.utils
            post.total = Articulos.objects.filter(descripcion=post.articulos).first().precio #Asigno precio en base a la descripcion seleccionada. Puede tener fallas esto. Ver Ajax o Select2 para mejorar formulario
            post.save()
            #Elegir retorno, mostrar que se agrego correctamente la venta por ejemplo...
            return ventas(request)
    else:
        form = VentaForm()

    return render(request, 'venta_new.html', {'form': form})

#Para modificacion de datos de articulo
def venta_edit(request, id_venta):
    #pk = primary key, identificador en DB
    post = get_object_or_404(Relaciones, pk=id_venta)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #Elegir retorno, mostrar que se modifico correctamente la venta por ejemplo...
            return ventas(request)
    else:
        form = VentaForm(instance=post)
    return render(request, 'venta_edit.html', {'form': form, 'id_venta':id_venta})

def venta_delete(request, id_venta):
    #Ver si hace falta confirmacion o algo...
    post = get_object_or_404(Relaciones, pk=id_venta)
    post.delete()          
    return ventas(request)

def articulos(request):
    articulos = Articulos.objects.all()
    return render(request, "articulos.html", {'articulos':articulos})

def articulo_new(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #Elegir retorno, mostrar que se agrego correctamente el articulo por ejemplo...
            return articulos(request)
    else:
        form = ArticuloForm()

    return render(request, 'articulo_new.html', {'form': form})

#Para modificacion de datos de articulo
def articulo_edit(request, id_articulo):
    #pk = primary key, identificador en DB
    post = get_object_or_404(Articulos, pk=id_articulo)
    if request.method == "POST":
        form = ArticuloForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #Elegir retorno, mostrar que se modifico correctamente el cliente por ejemplo...
            return articulos(request)
    else:
        form = ArticuloForm(instance=post)
    return render(request, 'articulo_edit.html', {'form': form, 'id_articulo':id_articulo})

def articulo_delete(request, id_articulo):
    #Ver si hace falta confirmacion o algo...
    post = get_object_or_404(Articulos, pk=id_articulo)
    post.delete()          
    return articulos(request)
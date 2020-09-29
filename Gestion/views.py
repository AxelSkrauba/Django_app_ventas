#Para vistas basadas en clases
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from Gestion.models import Clientes, Articulos, Relaciones
from .forms import ClienteForm, ArticuloForm, VentaForm

class Principal(TemplateView):
    #Herencia de TemplateView, facil:
    template_name = 'principal.html'
    #Usando get seria: (Pero por defecto ya lo hace)
    #def get(self, request, *args, **kwars):
    #    return render(request, "principal.html")

class Default(TemplateView):
    template_name = 'default.html'

#Para listar clientes
class Clientes_v(ListView):
    #Usa get por defecto:
    model = Clientes
    template_name = 'clientes.html'
    context_object_name = 'clientes'
    #Por defecto hace esta consulta, modificar para otra
    #queryset = Clientes.objects.all()
    #paginate_by = 25   #Renderiza la cantidad dada

#Para nuevo cliente
class Cliente_new(CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'cliente_new.html'
    success_url = reverse_lazy('clientes')

#Para modificacion de datos de cliente
class Cliente_edit(UpdateView):
    model = Clientes
    form_class = ClienteForm
    template_name = 'cliente_edit.html'
    success_url = reverse_lazy('clientes')

#Para eliminar cliente
class Cliente_delete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes')

class Ventas(ListView):
    model = Relaciones
    template_name = 'ventas.html'
    context_object_name = 'ventas'

class Venta_new(CreateView):
    model = Relaciones
    form_class = VentaForm
    template_name = 'venta_new.html'
    success_url = reverse_lazy('ventas')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.fecha = timezone.now() #from django.utils
        instance.total = Articulos.objects.filter(descripcion=instance.articulos).first().precio #Asigno precio en base a la descripcion seleccionada. Puede tener fallas esto. Ver Ajax o Select2 para mejorar formulario
        instance.save()
        return super().form_valid(form)

class Venta_edit(UpdateView):
    model = Relaciones
    form_class = VentaForm
    template_name = 'venta_edit.html'
    success_url = reverse_lazy('ventas')

class Venta_delete(DeleteView):
    model = Relaciones
    success_url = reverse_lazy('ventas')

class Articulos_v(ListView):
    model = Articulos
    template_name = 'articulos.html'
    context_object_name = 'articulos'

class Articulo_new(CreateView):
    model = Articulos
    form_class = ArticuloForm
    template_name = 'articulo_new.html'
    success_url = reverse_lazy('articulos')

class Articulo_edit(UpdateView):
    model = Articulos
    form_class = ArticuloForm
    template_name = 'articulo_edit.html'
    success_url = reverse_lazy('articulos')

class Articulo_delete(DeleteView):
    model = Articulos
    success_url = reverse_lazy('articulos')
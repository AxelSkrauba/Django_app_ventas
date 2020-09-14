from django import forms
from .models import Clientes, Articulos, Relaciones

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('nombre', 'apellido', 'dni', 'email',)
       
class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulos
        fields = ('codigo', 'descripcion', 'precio',)

class VentaForm(forms.ModelForm):
    cliente = forms.Select()
    articulos = forms.Select()

    class Meta:
        model = Relaciones
        fields = ('cliente', 'articulos',)

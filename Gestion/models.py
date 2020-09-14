from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    email = models.EmailField()

    class Meta:
        ordering = ["apellido"]

    def nombreCompleto(self):
        nombreCompleto = '{} {}'.format(self.nombre,self.apellido)
        return nombreCompleto

    def __str__(self):
        return self.nombreCompleto()

class Articulos(models.Model):
    descripcion = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Relaciones(models.Model):
    #Decidir que pasa en caso de que se elimine un artículo o cliente referenciado... Si se borra cliente, se borra referencia por ahora.
    fecha = models.DateField()
    #cliente = models.CharField(max_length=100)
    cliente = models.ForeignKey(Clientes, null=False, blank=False, on_delete=models.CASCADE)
    #articulos = models.TextField()
    articulos = models.ForeignKey(Articulos, null=True, blank=False, on_delete=models.SET_NULL)
    total = models.IntegerField()

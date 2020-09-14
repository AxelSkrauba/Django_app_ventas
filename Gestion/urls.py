from django.urls import path
from Gestion import views

urlpatterns = [
    path('', views.principal, name="home"),
    path('default/', views.default, name="default"),
    path('clientes/', views.clientes, name="clientes"),
    path('cliente/new/', views.cliente_new, name="cliente_new"),
    path('cliente/<int:id_cliente>', views.cliente_edit, name="cliente_edit"),
    path('cliente/delete/<int:id_cliente>', views.cliente_delete, name="cliente_delete"),
    path('ventas/', views.ventas, name="ventas"),
    path('venta/new/', views.venta_new, name="venta_new"),
    path('venta/<int:id_venta>', views.venta_edit, name="venta_edit"),
    path('venta/delete/<int:id_venta>', views.venta_delete, name="venta_delete"),
    path('articulos/', views.articulos, name="articulos"),
    path('articulo/new/', views.articulo_new, name="articulo_new"),
    path('articulo/<int:id_articulo>', views.articulo_edit, name="articulo_edit"),
    path('articulo/delete/<int:id_articulo>', views.articulo_delete, name="articulo_delete"),

]
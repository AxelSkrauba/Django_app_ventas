from django.urls import path
from Gestion import views

urlpatterns = [
    path('', views.Principal.as_view(), name="home"),
    path('default/', views.Default.as_view(), name="default"),
    path('clientes/', views.Clientes_v.as_view(), name="clientes"),
    path('cliente/new/', views.Cliente_new.as_view(), name="cliente_new"),
    path('cliente/<int:pk>', views.Cliente_edit.as_view(), name="cliente_edit"),
    path('cliente/delete/<int:pk>', views.Cliente_delete.as_view(), name="cliente_delete"),
    path('ventas/', views.Ventas.as_view(), name="ventas"),
    path('venta/new/', views.Venta_new.as_view(), name="venta_new"),
    path('venta/<int:pk>', views.Venta_edit.as_view(), name="venta_edit"),
    path('venta/delete/<int:pk>', views.Venta_delete.as_view(), name="venta_delete"),
    path('articulos/', views.Articulos_v.as_view(), name="articulos"),
    path('articulo/new/', views.Articulo_new.as_view(), name="articulo_new"),
    path('articulo/<int:pk>', views.Articulo_edit.as_view(), name="articulo_edit"),
    path('articulo/delete/<int:pk>', views.Articulo_delete.as_view(), name="articulo_delete"),

]
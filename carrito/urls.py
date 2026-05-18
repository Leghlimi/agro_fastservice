from django.urls import path
from . import views

app_name = 'carrito'
'''
app_name sirve para identificar en las plantillas y hacer todo más legible.
p. ejemplo {% url 'carrito:limpiar%}: usa app_name 'carrito' y luego de carrito utilicve su url 'limpiar'.
Esto es debido a que si existe otro app con la función limpiar (servicios_limpiar p. ejemplo) 
entrarían las urls en conflicto, con app_name, todo está correctamente identificado.
La url se forma con app_name/name.
'''

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:servicio_id>/', views.agregar_al_carrito, name='agregar'),
    path('eliminar/<int:servicio_id>/', views.eliminar_del_carrito, name='eliminar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
]
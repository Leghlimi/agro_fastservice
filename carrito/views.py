from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from servicios.models import Servicio
from .models import Carrito, ItemCarrito

@login_required
def agregar_al_carrito(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, servicio=servicio)
    if not creado:
        item.cantidad += 1
        messages.info(request, f"Se ha aumentado la cantidad de {servicio.nombre} en el carrito.")
    else:
        messages.success(request, f"Producto '{servicio.nombre}' añadido al carrito correctamente.")
    item.save()

    return redirect('servicios:detalle_servicio', pk=servicio_id)

@login_required
def eliminar_del_carrito(request, servicio_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item = carrito.items.filter(servicio_id=servicio_id).first()
    if item:
        item.delete()
        messages.warning(request, f"Producto '{item.servicio.nombre}' eliminado del carrito.")
    else:
        messages.error(request, "El producto no se encontró en el carrito.")
    return redirect('carrito:ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    if carrito.items.exists():
        carrito.items.all().delete()
        messages.warning(request, "Se han eliminado todos los productos del carrito.")
    else:
        messages.info(request, "El carrito ya estaba vacío.")
    return redirect('carrito:ver_carrito')

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.select_related('servicio') # obtiene los items con sus servicios
    total = carrito.total_precio()
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'items': items, 'total': total})

'''
Relacion con el modelo:
views.py consulta → Servicio (para obtener el servicio)
views.py consulta → Carrito (para obtener o crear el carrito del usuario)
views.py consulta → ItemCarrito (para obtener o crear el item)
'''
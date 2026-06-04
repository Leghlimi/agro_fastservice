from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from servicios.models import Servicio
from .models import Carrito, ItemCarrito

@login_required
def agregar_al_carrito(request, servicio_id):
    """
    Añade un servicio al carrito del usuario autenticado.

    Busca el servicio por su id. Si el usuario no tiene carrito lo crea.
    Si el servicio ya está en el carrito incrementa su cantidad en 1,
    si no existe lo añade con cantidad 1.

    :param request: La petición HTTP de Django.
    :param servicio_id: Id del servicio a añadir al carrito.
    :return: Redirección al detalle del servicio.
    """
    '''
    carrito, _ : get_or_create devolverá una tupla -> (objeto, true/false), como solo quiero el objeto, el guión bajo descartará el boolean.
    item, creado : get_or_create igual que antes. Buscar si el servicio ya está en el carrito y si no está lo va a crear.
    Si ya existe lo reutiliza. Aquí sí se usa el boolean (item:objeto, creado:boolean).
    Esto es para que no se creen dos items distintos del mismo servicio, sino que se incremente la cantidad.
    '''
    servicio = get_object_or_404(Servicio, id=servicio_id)
    cantidad_raw = request.POST.get('cantidad', '').strip()
    cantidad = int(cantidad_raw) if cantidad_raw else 1
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, servicio=servicio)
    if not creado:
        item.cantidad += cantidad
        messages.info(request, f"Se han añadido {cantidad} kg más de {servicio.nombre} al carrito.")
    else:
        item.cantidad = cantidad
        messages.success(request, f"Servicio '{servicio.nombre}' añadido con {cantidad} kg.")
    item.save()

    return redirect('servicios:detalle_servicio', pk=servicio_id)

@login_required
def eliminar_del_carrito(request, servicio_id):
    """
    Elimina un servicio del carrito del usuario autenticado.

    Busca el item en el carrito por el id del servicio y lo elimina.
    Si el item no existe muestra un mensaje de error.

    :param request: La petición HTTP de Django.
    :param servicio_id: Id del servicio a eliminar del carrito.
    :return: Redirección a la vista del carrito.
    """
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
    """
    Elimina todos los items del carrito del usuario autenticado.

    Si el carrito tiene items los elimina todos de una vez.
    Si el carrito ya está vacío muestra un mensaje informativo.

    :param request: La petición HTTP de Django.
    :return: Redirección a la vista del carrito.
    """
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    if carrito.items.exists():
        carrito.items.all().delete()
        messages.warning(request, "Se han eliminado todos los productos del carrito.")
    else:
        messages.info(request, "El carrito ya estaba vacío.")
    return redirect('carrito:ver_carrito')

@login_required
def ver_carrito(request):
    """
    Muestra el contenido del carrito del usuario autenticado.

    Obtiene el carrito del usuario, sus items con los servicios asociados
    y el precio total. Si el usuario no tiene carrito lo crea vacío.

    :param request: La petición HTTP de Django.
    :return: HttpResponse con el template 'carrito/ver_carrito.html'
             renderizado con el carrito, items y total en el contexto.
    """
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user) # busca el carrito del usuario, si no lo encuentra lo crea.
    items = carrito.items.select_related('servicio') # obtiene todos los ItemCarrito asociados a ese Carrito (todas las agrupaciones de un mismo servicio).
    total = carrito.total_precio()
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'items': items, 'total': total})

'''
Relacion con el modelo:
views.py consulta → Servicio (para obtener el servicio)
views.py consulta → Carrito (para obtener o crear el carrito del usuario)
views.py consulta → ItemCarrito (para obtener o crear el item)
'''

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from servicios.models import Servicio

def lista_servicios(request):
    servicios = Servicio.objects.all().order_by('id')  # mantenemos un orden consistente
    paginator = Paginator(servicios, 6)  # mostramos 6 servicios por página

    # Obtenemos el número de página desde la URL (?page=2)
    page_number = request.GET.get('page')

    # Obtenemos los objetos de esa página
    page_obj = paginator.get_page(page_number)

    # Pasamos a la plantilla como 'lista_servicios'
    contexto_catalogo_servicios = {'lista_servicios': page_obj}
    return render(request, 'catalogo/lista_servicios.html', contexto_catalogo_servicios)

def detalle_servicio(request, pk):
    # Obtenemos el servicio concreto o mostramos un 404 si no existe
    servicio = get_object_or_404(Servicio, pk=pk)

    # Creamos el contexto que pasaremos a la plantilla
    contexto = {'servicio': servicio}

    # Renderizamos la plantilla de detalle
    return render(request, 'catalogo/detalle_servicio.html', contexto)

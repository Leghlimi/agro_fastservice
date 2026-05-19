
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from servicios.models import Servicio

''''
# Sin paginator->
def lista_servicios(request):
    servicios = Servicio.objects.all()
    contexto_servicios_servicios = {'lista_servicios': servicios}
    return render(request, 'servicios/lista_servicios.html', contexto_servicios_servicios)
'''

def lista_servicios(request):
    """
    Muestra el catálogo de servicios agrícolas paginado.

    Una función que obtiene un QuerySet del Model/BD, y lo inyecta en HTML con render.
    Obtiene todos los servicios de la base de datos ordenados por ID
    y los divide en páginas de 3 elementos. El número de página se
    lee desde la URL mediante el parámetro ?page=2.

    Args:
        request: La petición HTTP de Django.

    Returns:
        HttpResponse con el template 'servicios/lista_servicios.html'
        renderizado, incluyendo el objeto de página como 'lista_servicios'.
    """
    servicios = Servicio.objects.all().order_by('id')  # QuerySet con todos los servicios, mantenemos un orden consistente
    paginator = Paginator(servicios, 4)  # mostramos x servicios por página

    # Obtenemos el número de página desde la URL (?page=2)
    page_number = request.GET.get('page')

    # Obtenemos los objetos de esa página. Extrae solo los objetos de esa página. # page_obj es un objeto especial de Django
    page_obj = paginator.get_page(page_number)

    # Pasamos a la plantilla como 'lista_servicios'
    contexto_catalogo_servicios = {'lista_servicios': page_obj}
    return render(request, 'servicios/lista_servicios.html', contexto_catalogo_servicios)

def detalle_servicio(request, pk):
    """
    Muestra el detalle de un servicio concreto.

    Obtiene un objeto Servicio de la BD mediante su clave primaria (pk).
    Si el servicio no existe, devuelve automáticamente un error 404.

    :param request: La petición HTTP de Django.
    :param pk: Clave primaria del servicio a mostrar.
    :return: HttpResponse con el template 'servicios/detalle_servicio.html'
             renderizado, con el objeto 'servicio' en el contexto.
    """
    # Obtenemos el servicio concreto o mostramos un 404 si no existe
    servicio = get_object_or_404(Servicio, pk=pk)
    '''
    Una variable servicio que obtiene el objeto de un servicio concreto
    pasandole el modelo Servicio y una primary key (pk).
    '''
    # Creamos el contexto que pasaremos a la plantilla
    contexto = {'servicio': servicio}

    # Renderizamos la plantilla de detalle
    return render(request, 'servicios/detalle_servicio.html', contexto)



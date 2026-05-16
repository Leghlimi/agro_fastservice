from django.shortcuts import render
from servicios.models import Servicio
from django.core.paginator import Paginator
from django.db.models import Q

def buscar_servicios(request):
    """
    Se encargará de buscar objetos de tipo Servicio, según lo que busque el usuario.
    Recibir la peticion del usuario, procesar el término de búsqueda introducido por el usuario,
    obtener los resultados correspondientes de la BD, y mostrarlos en la plantilla adecuada.

    Recibe el parámetro 'q' desde la URL (?q=torillo), filtra los servicios
    por nombre o categoria, y devuelve los resultados paginados de 3 en 3.

    :param request: La petición HTTP de Django, debe contener el parámetro GET 'q'.
    :return: HttpResponse con el template 'buscador/resultados_busqueda.html'
             renderizado, con 'query' y 'lista_servicios' en el contexto.
    """
    query = request.GET.get('q', '')  # obtenemos el término de búsqueda

    # Filtrar por nombre o plataforma que contenga la query
    resultados = Servicio.objects.filter(
        Q(nombre__icontains=query) | Q(categoria__icontains=query)
    ).order_by('id')

    paginator = Paginator(resultados, 3)  # 3 servicios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'query': query,
        'lista_servicios': page_obj
    }

    return render(request, 'buscador/resultados_busqueda.html', contexto)

# request.GET.get('q', '')
# Lee el parámetro q de la URL. Si el usuario busca "torillo", la URL sería ?q=torillo y query valdría 'torillo'.
# El '' es el valor por defecto si no hay nada en la URL.

# Q() → es un objeto de Django que representa una condición. Se importa con from django.db.models import Q

# Q(nombre__icontains=query) | Q(categoria__icontains=query)  es el equivalente (Django) a
# WHERE nombre LIKE '%torillo%' OR categoria LIKE '%torillo%'
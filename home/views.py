from django.shortcuts import render

# Vista de la página principal (index)
def index(request):
    # render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

# Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

# La respuesta son archivos html en una ruta concreta
# Mostramos una plantilla html a partir de una solicitud
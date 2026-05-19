from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm

# Vista de la página principal (index)
def index(request):
    # render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

# Vista de la página de contacto
def contacto(request):
    """
    Gestiona el formulario de contacto.

    Si la petición es POST valida el formulario y guarda el mensaje en la BD.
    Si la petición es GET muestra el formulario vacío.

    :param request: La petición HTTP de Django.
    :return: HttpResponse con el template 'home/contacto.html' o
             redirección a 'home' si el envío es correcto.
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensaje enviado correctamente. Nos pondremos en contacto contigo pronto.")
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request, 'home/contacto.html', {'form': form})

def galeria(request):
    return render(request, 'home/galeria.html')
import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm, ConsultaForm

logger = logging.getLogger(__name__)


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
            mensaje = form.save()  # guarda en BD Y devuelve el objeto guardado
            try:
                send_mail(
                    subject=f'Nueva consulta de {mensaje.nombre}',
                    message=(
                        f'Nombre: {mensaje.nombre}\n'
                        f'Teléfono: {mensaje.telefono}\n'
                        f'Email: {mensaje.email}\n'
                        f'Fecha: {mensaje.fecha}\n'
                        f'Dirección: {mensaje.direccion_finca}\n'
                        f'M2 finca: {mensaje.m2_finca}\n'
                        f'Kg estimados: {mensaje.kg_estimados}\n'
                        f'Otros datos: {mensaje.otros_datos}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['agrofastservice@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                # El mensaje ya está guardado en la BD; solo fallamos el envío de correo.
                # Avisamos al usuario igualmente pero dejamos constancia en logs.
                logger.error("Error al enviar el correo de contacto: %s", e)
            messages.success(request, "Mensaje enviado correctamente. Nos pondremos en contacto contigo pronto.")
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request, 'home/contacto.html', {'form': form})


def galeria(request):
    return render(request, 'home/galeria.html')


def consulta(request):
    enviado = False
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            try:
                send_mail(
                    subject=f'Nueva consulta rápida de {mensaje.nombre}',
                    message=(
                        f'Nombre: {mensaje.nombre}\n'
                        f'Teléfono: {mensaje.telefono}\n'
                        f'Mensaje: {mensaje.mensaje}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['agrofastservice@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error("Error al enviar el correo de consulta: %s", e)
            enviado = True
            messages.success(request, "Consulta enviada correctamente. Te contactaremos pronto.")
            form = ConsultaForm()
    else:
        form = ConsultaForm()
    return render(request, 'home/consulta.html', {'form': form, 'enviado': enviado})


# Sin envio de email
# def consulta(request):
#     enviado = False
#     if request.method == 'POST':
#         form = ConsultaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             enviado = True
#             form = ConsultaForm()
#     else:
#         form = ConsultaForm()
#     return render(request, 'home/consulta.html', {'form': form, 'enviado': enviado})

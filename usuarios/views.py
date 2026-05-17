from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages

def registro_view(request):
    """
    Gestiona el registro de nuevos usuarios.

    Si la petición es POST valida el formulario, guarda el usuario en la BD,
    inicia sesión automáticamente y redirige a inicio.
    Si la petición es GET muestra el formulario vacío.

    :param request: La petición HTTP de Django.
    :return: HttpResponse con el template 'usuarios/registro.html' o
             redirección a 'home' si el registro es correcto.
    """
    if request.method == 'POST':                # ¿el usuario ha enviado el formulario?
        form = RegistroForm(request.POST)       # recoge los datos
        if form.is_valid():                     # ¿los datos son válidos?
            usuario = form.save()               # guarda en la BD
            login(request, usuario)             # inicia sesión automáticamente
            messages.success(request, "Registro completado correctamente.") # muestra mensaje de éxito
            return redirect('home')             # redirige a inicio
    else:
        form = RegistroForm()                   # muestra el formulario vacío
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    """
    Gestiona el inicio de sesión de usuarios.

    Si la petición es POST valida las credenciales, inicia la sesión
    y redirige a inicio. Si las credenciales son incorrectas muestra
    un mensaje de error.
    Si la petición es GET muestra el formulario vacío.

    :param request: La petición HTTP de Django.
    :return: HttpResponse con el template 'usuarios/login.html' o
             redirección a 'home' si el login es correcto.
    """
    if request.method == 'POST':                # ¿el usuario ha enviado el formulario?
        form = LoginForm(request, data=request.POST) # recoge los datos, necesita 'request' para gestionar la sesión
        if form.is_valid():                     # ¿las credenciales son correctas?
            usuario = form.get_user()           # obtiene el objeto usuario autenticado
            login(request, usuario)             # inicia la sesión, crea la cookie de sesión
            messages.success(request, "Inicio de sesión correcto.") # muestra mensaje de éxito
            return redirect('home')             # redirige a inicio
        else:                                   # credenciales incorrectas, muestra error
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:                                       # muestra el formulario vacío
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    """
    Gestiona el cierre de sesión del usuario.

    Cierra la sesión activa, muestra un mensaje informativo
    y redirige a la página de inicio.

    :param request: La petición HTTP de Django.
    :return: Redirección a 'home'.
    """
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('home')

#login_required es un decorador de Django que antes de ejecutar perfil_view comprueba si el usuario está autenticado
@login_required
def perfil_view(request):
    """
    Muestra el perfil del usuario autenticado.

    El decorador @login_required redirige automáticamente al login
    si el usuario no está autenticado.

    :param request: La petición HTTP de Django.
    :return: HttpResponse con el template 'usuarios/perfil.html'.
    """
    return render(request, 'usuarios/perfil.html')

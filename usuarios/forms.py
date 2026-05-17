from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', ]

class LoginForm(AuthenticationForm):
    # No hace falta Meta
    pass

'''
En RegistroForm especificamos los campos  porque necesitamos definir qué datos del usuario 
vamos a registrar,mientras que en LoginForm no hace falta porque Django
ya incluye por defecto los campos de usuario y contraseña para iniciar sesión.
'''
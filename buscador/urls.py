from django.urls import path
from . import views

# path vacío ''. Se monta a partir de buscador/ de urls.py principal
urlpatterns = [
    path('', views.buscar_servicios, name='buscar_servicios'),
]
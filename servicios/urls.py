from django.urls import path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('', views.lista_servicios, name='lista_servicios'),
    path('<int:pk>/', views.detalle_servicio, name='detalle_servicio'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # 👈 ruta principal: llama a la vista index
    path('contacto/', views.contacto, name='contacto'),  # 👈 ruta contacto: llama a la vista contacto
]
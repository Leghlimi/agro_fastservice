from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=3)
    categoria = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200, default="default.png")

    def __str__(self):
        return self.nombre


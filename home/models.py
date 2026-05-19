from django.db import models

class MensajeContacto(models.Model):
    """
    Modelo que representa una consulta de contacto enviada por un usuario.

    Attributes:
        nombre: Nombre completo del remitente.
        telefono: Teléfono de contacto.
        email: Email del remitente.
        fecha: Fecha solicitada para el servicio.
        direccion_finca: Dirección de la finca.
        m2_finca: Superficie de la finca en m2.
        kg_estimados: Kilos estimados de producción.
        otros_datos: Información adicional.
        enviado_en: Fecha de envío, se asigna automáticamente.
    """
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha = models.DateField()
    direccion_finca = models.CharField(max_length=200)
    m2_finca = models.PositiveIntegerField(blank=True, null=True)
    kg_estimados = models.PositiveIntegerField(blank=True, null=True)
    otros_datos = models.TextField(blank=True, default='')
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"

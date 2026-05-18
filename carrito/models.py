from django.db import models
from django.conf import settings
from servicios.models import Servicio

class Carrito(models.Model):
    """
    Modelo que representa el carrito de compra de un usuario.

    Cada usuario tiene exactamente un carrito. Almacena los servicios
    seleccionados antes de agendar una cita.

    Attributes:
        usuario: Usuario propietario del carrito, relación uno a uno.
        creado: Fecha de creación del carrito, se asigna automáticamente.
        actualizado: Fecha de última modificación, se actualiza automáticamente.
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carrito'
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrito de compra {self.usuario.username}"

    def total_items(self):
        """
        Calcula la cantidad total de items en el carrito.

        :return: Entero con la suma de las cantidades de todos los items.
        """
        return self.items.count()

    def total_precio(self):
        """
        Calcula el precio total del carrito.

        :return: Decimal con la suma de los subtotales de todos los items.
        """
        return sum(item.subtotal() for item in self.items.all())


class ItemCarrito(models.Model):
    """
    Modelo que representa un elemento individual del carrito.

    Relaciona un servicio con su cantidad dentro de un carrito concreto.
    No puede haber dos items del mismo servicio en el mismo carrito.

    Attributes:
        carrito: Carrito al que pertenece el item.
        servicio: Servicio asociado al item.
        cantidad: Número de unidades del servicio, mínimo 1.
    """
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('carrito', 'servicio')

    def __str__(self):
        return f"{self.servicio.nombre} x {self.cantidad} kg"

    def subtotal(self):
        """
        Calcula el subtotal del item.

        :return: Decimal resultado de multiplicar precio por cantidad.
        """
        return self.servicio.precio * self.cantidad

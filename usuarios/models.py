from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser.

    Sobreescribe el campo email para hacerlo único y redefine
    groups y user_permissions para evitar conflictos de reverse
    accessors con el modelo de usuario por defecto de Django.

    Attributes:
        email: Email del usuario, debe ser único en la BD.
        groups: Grupos a los que pertenece el usuario.
        user_permissions: Permisos específicos del usuario.
    """
    email = models.EmailField(unique=True)

    # Evitar conflictos de reverse accessors
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_set',  # aquí cambia el related_name
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',  # aquí cambia el related_name
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

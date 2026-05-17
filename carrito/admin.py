from django.contrib import admin
from .models import Carrito, ItemCarrito

# Inline para mostrar los ítems dentro del carrito
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0  # No mostrar filas vacías adicionales
    readonly_fields = ('subtotal',)  # Subtotal solo lectura

# Admin del carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total_items', 'total_precio', 'creado', 'actualizado')
    search_fields = ('usuario__username',)  # Buscar carritos por nombre de usuario
    inlines = [ItemCarritoInline]

# Admin de los ítems (opcional, también accesible por separado)
@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'servicio', 'cantidad', 'subtotal')
    list_filter = ('carrito',)
    search_fields = ('servicio__nombre',)
    readonly_fields = ('subtotal',)

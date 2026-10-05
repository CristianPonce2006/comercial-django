from django.db import models
from .categoria import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="descripcion"
    )
    precio_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio de compra",
        )
    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio de venta",
        )
    stock = models.PositiveIntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="productos", verbose_name="Categoría"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de actualización")
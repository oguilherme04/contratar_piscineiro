from django.db import models
from cliente.models import Cliente

class Piscina(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="piscinas")
    volume = models.FloatField()
    tipo = models.CharField(max_length=50)
    privada = models.BooleanField(default=True)

    def __str__(self):
        return f"Piscina de {self.cliente} ({self.tipo})"
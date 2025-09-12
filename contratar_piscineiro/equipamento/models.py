from django.db import models
from piscineiro.models import Piscineiro

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    proprietario = models.ForeignKey(Piscineiro, on_delete=models.CASCADE, related_name="equipamentos")

    def __str__(self):
        return f"{self.nome} ({self.marca}/{self.modelo})"
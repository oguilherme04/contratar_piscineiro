from django.db import models
from piscina.models import Piscina
from piscineiro.models import Piscineiro
from equipamento.models import Equipamento
from cliente.models import Cliente

class Manutencao(models.Model):
    piscina = models.ForeignKey('piscina.Piscina', on_delete=models.CASCADE, related_name="manutencoes")
    piscineiro = models.ForeignKey('piscineiro.Piscineiro', on_delete=models.CASCADE, related_name="manutencoes")
    equipamento = models.ForeignKey('equipamento.Equipamento', on_delete=models.CASCADE, related_name="manutencoes")
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, related_name="manutencoes")
    tipo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return f"Manutenção {self.tipo} - {self.piscina}"
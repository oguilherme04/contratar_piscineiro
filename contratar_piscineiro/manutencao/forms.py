from django.forms import ModelForm
from .models import Manutencao

class ManutencaoForm(ModelForm):
    class Meta:
        model = Manutencao
        fields = ["piscina", "piscineiro", "equipamento", "tipo", "data_inicio", "data_fim", "observacoes"]

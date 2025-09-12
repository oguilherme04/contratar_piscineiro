from django.forms import ModelForm
from .models import Equipamento

class EquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "descricao", "marca", "modelo", "proprietario"]
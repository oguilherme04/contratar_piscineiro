from django.forms import ModelForm
from .models import Piscina

class PiscinaForm(ModelForm):
    class Meta:
        model = Piscina
        fields = ["cliente", "volume", "tipo", "privada"]
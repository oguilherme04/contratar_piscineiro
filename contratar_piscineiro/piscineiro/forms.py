from django.forms import ModelForm
from .models import Piscineiro

class PiscineiroForm(ModelForm):
    class Meta:
        model = Piscineiro
        fields = ['cpf_cnpj', 'telefone', 'experiencia', 'disponibilidade']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'disponibilidade':
                field.widget.attrs.update({'class': 'form-control'})
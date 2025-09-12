from django.db import models
from django.contrib.auth.models import User

class Piscineiro(User):
    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    disponibilidade = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Piscineiro'
        verbose_name_plural = 'Piscineiros'

    @classmethod
    def create_user(cls, username, email, first_name, last_name, password, **extra_fields):
        user = cls(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def __str__(self):
        name = self.get_full_name() or self.username
        status = "Disponível" if self.disponibilidade else "Indisponível"
        cpf_display = self.cpf_cnpj if self.cpf_cnpj else "Sem CPF/CNPJ"
        return f"{name} - {status} ({cpf_display})"
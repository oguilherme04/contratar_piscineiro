from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Cliente(User):
    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

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
        cpf_display = self.cpf_cnpj if self.cpf_cnpj else "Sem CPF/CNPJ"
        return f"{name} ({cpf_display})"
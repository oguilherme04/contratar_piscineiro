from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from cliente.models import Cliente
from piscineiro.models import Piscineiro
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def about(request):
    return render(request, "about.html")

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    is_piscineiro = forms.BooleanField(required=False, label='Sou Piscineiro')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    is_piscineiro = form.cleaned_data.get('is_piscineiro', False)
                    
                    if is_piscineiro:
                        piscineiro = Piscineiro.create_user(
                            username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            password=form.cleaned_data['password1']
                        )
                        login(request, piscineiro)
                        return redirect('piscineiro_add')
                    else:
                        cliente = Cliente.create_user(
                            username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            password=form.cleaned_data['password1']
                        )
                        login(request, cliente)
                        return redirect('cliente_add')
            except Exception as e:
                form.add_error(None, f'Erro ao criar usuário: {str(e)}')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form}) 
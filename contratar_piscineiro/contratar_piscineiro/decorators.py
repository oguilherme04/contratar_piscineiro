from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps
from cliente.models import Cliente
from piscineiro.models import Piscineiro
from django.contrib.auth.models import User

def cliente_required(view_func):
    """
    Decorator que verifica se o usuário está autenticado e é um cliente
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        try:
            cliente = Cliente.objects.get(id=request.user.id)
            return view_func(request, *args, **kwargs)
        except Cliente.DoesNotExist:
            pass
        
        return HttpResponseForbidden("Acesso restrito a clientes")
    
    return _wrapped_view

def piscineiro_required(view_func):
    """
    Decorator que verifica se o usuário está autenticado e é um piscineiro
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        try:
            piscineiro = Piscineiro.objects.get(id=request.user.id)
            return view_func(request, *args, **kwargs)
        except Piscineiro.DoesNotExist:
            pass
        
        return HttpResponseForbidden("Acesso restrito a piscineiros")
    
    return _wrapped_view

def admin_required(view_func):
    """
    Decorator que verifica se o usuário é admin
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        
        return HttpResponseForbidden("Acesso restrito a administradores")
    
    return _wrapped_view

def user_is_cliente(user):
    """
    Função auxiliar para verificar se um usuário é cliente
    """
    if not user.is_authenticated:
        return False
    try:
        Cliente.objects.get(id=user.id)
        return True
    except Cliente.DoesNotExist:
        return False

def user_is_piscineiro(user):
    """
    Função auxiliar para verificar se um usuário é piscineiro
    """
    if not user.is_authenticated:
        return False
    try:
        Piscineiro.objects.get(id=user.id)
        return True
    except Piscineiro.DoesNotExist:
        return False

def user_is_admin(user):
    """
    Função auxiliar para verificar se um usuário é admin
    """
    return user.is_authenticated and user.is_superuser
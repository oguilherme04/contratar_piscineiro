from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Piscina
from .forms import PiscinaForm
from contratar_piscineiro.decorators import user_is_cliente, user_is_admin

@login_required
def index(request):
    piscinas = Piscina.objects.all()
    
    can_edit = user_is_cliente(request.user) or user_is_admin(request.user)
    can_delete = user_is_cliente(request.user) or user_is_admin(request.user)
    can_add = user_is_cliente(request.user) or user_is_admin(request.user)
    
    return render(request, 'piscina/index.html', {
        'piscinas': piscinas,
        'can_edit': can_edit,
        'can_delete': can_delete,
        'can_add': can_add
    })

@login_required
def add(request):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")
    
    if request.method == 'POST':
        form = PiscinaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/piscina/')
    else:
        form = PiscinaForm()
    return render(request, 'piscina/add.html', {'form': form})

@login_required
def edit(request, id_piscina):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")
    
    piscina = get_object_or_404(Piscina, id=id_piscina)
    if request.method == 'POST':
        form = PiscinaForm(request.POST, instance=piscina)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/piscina/')
    else:
        form = PiscinaForm(instance=piscina)
    return render(request, 'piscina/edit.html', {'form': form})

@login_required
def delete(request, id_piscina):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")
    
    piscina = get_object_or_404(Piscina, id=id_piscina)
    if request.method == 'POST':
        piscina.delete()
        return redirect('piscina_index')
    return render(request, 'piscina/delete.html', {'piscina': piscina})

@login_required
def detalhe(request, id_piscina):
    piscina = get_object_or_404(Piscina, id=id_piscina)
    return render(request, 'piscina/detalhe.html', {'piscina': piscina})
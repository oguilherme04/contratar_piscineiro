from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Manutencao
from .forms import ManutencaoForm
from contratar_piscineiro.decorators import user_is_cliente, user_is_admin

@login_required
def index(request):
    manutencoes = Manutencao.objects.all()
    
    can_edit = user_is_cliente(request.user) or user_is_admin(request.user)
    can_delete = user_is_cliente(request.user) or user_is_admin(request.user)
    can_add = user_is_cliente(request.user) or user_is_admin(request.user)
    
    return render(request, 'manutencao/index.html', {
        'manutencoes': manutencoes,
        'can_edit': can_edit,
        'can_delete': can_delete,
        'can_add': can_add
    })

@login_required
def add(request):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")
    
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            if hasattr(request.user, 'cliente'):
                manutencao.cliente = request.user.cliente
            manutencao.save()
            return HttpResponseRedirect('/manutencao/')
    else:
        form = ManutencaoForm()
    return render(request, 'manutencao/add.html', {'form': form})

@login_required
def edit(request, id_manutencao):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")

    manutencao = get_object_or_404(Manutencao, id=id_manutencao)
    if request.method == 'POST':
        form = ManutencaoForm(request.POST, instance=manutencao)
        if form.is_valid():
            manutencao_editada = form.save(commit=False)
            if hasattr(request.user, 'cliente') and not manutencao_editada.cliente:
                manutencao_editada.cliente = request.user.cliente
            manutencao_editada.save()
            return HttpResponseRedirect('/manutencao/')
    else:
        form = ManutencaoForm(instance=manutencao)
    return render(request, 'manutencao/edit.html', {'form': form})

@login_required
def delete(request, id_manutencao):
    if not (user_is_cliente(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a clientes e administradores")

    manutencao = get_object_or_404(Manutencao, id=id_manutencao)
    if request.method == 'POST':
        manutencao.delete()
        return redirect('manutencao_index') 
    return render(request, 'manutencao/delete.html', {'manutencao': manutencao})

@login_required
def detalhe(request, id_manutencao):
    manutencao = get_object_or_404(Manutencao, id=id_manutencao)
    return render(request, 'manutencao/detalhe.html', {'manutencao': manutencao})
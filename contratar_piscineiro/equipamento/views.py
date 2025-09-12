from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Equipamento
from .forms import EquipamentoForm
from contratar_piscineiro.decorators import user_is_piscineiro, user_is_admin

@login_required
def index(request):
    equipamentos = Equipamento.objects.all()
    
    can_edit = user_is_piscineiro(request.user) or user_is_admin(request.user)
    can_delete = user_is_piscineiro(request.user) or user_is_admin(request.user)
    can_add = user_is_piscineiro(request.user) or user_is_admin(request.user)
    
    return render(request, 'equipamento/index.html', {
        'equipamentos': equipamentos,
        'can_edit': can_edit,
        'can_delete': can_delete,
        'can_add': can_add
    })

@login_required
def add(request):
    if not (user_is_piscineiro(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a piscineiros e administradores")
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipamento/')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/add.html', {'form': form})

@login_required
def edit(request, id_equipamento):
    if not (user_is_piscineiro(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a piscineiros e administradores")

    equipamento = get_object_or_404(Equipamento, id=id_equipamento)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipamento/')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/edit.html', {'form': form})

@login_required
def delete(request, id_equipamento):
    if not (user_is_piscineiro(request.user) or user_is_admin(request.user)):
        return HttpResponseForbidden("Acesso restrito a piscineiros e administradores")

    equipamento = get_object_or_404(Equipamento, id=id_equipamento)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipamento_index')
    return render(request, 'equipamento/delete.html', {'equipamento': equipamento})


@login_required
def detalhe(request, id_equipamento):  
    equipamento = get_object_or_404(Equipamento, id=id_equipamento)
    return render(request, 'equipamento/detalhe.html', {'equipamento': equipamento})
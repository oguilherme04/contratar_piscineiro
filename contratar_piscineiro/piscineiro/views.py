from django.shortcuts import render, get_object_or_404, redirect
from .models import Piscineiro
from .forms import PiscineiroForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from contratar_piscineiro.decorators import user_is_admin, user_is_piscineiro

@login_required
def index(request):
    piscineiros = Piscineiro.objects.all()
    
    can_edit = user_is_admin(request.user)
    can_delete = user_is_admin(request.user)
    can_add = user_is_piscineiro(request.user) and not Piscineiro.objects.filter(id=request.user.id).exists()
    
    return render(request, 'piscineiro/index.html', {
        'piscineiros': piscineiros,
        'can_edit': can_edit,
        'can_delete': can_delete,
        'can_add': can_add
    })

@login_required
def add(request):
    if not user_is_piscineiro(request.user):
        return HttpResponseForbidden("Acesso restrito a piscineiros")
    
    piscineiro = get_object_or_404(Piscineiro, id=request.user.id)
    
    if request.method == 'POST':
        form = PiscineiroForm(request.POST, instance=piscineiro)
        if form.is_valid():
            form.save()
            return redirect('piscineiro_index')
    else:
        form = PiscineiroForm(instance=piscineiro)
    return render(request, 'piscineiro/add.html', {'form': form})

@login_required
def detalhe(request, id_piscineiro): 
    piscineiro = get_object_or_404(Piscineiro, id=id_piscineiro)
    return render(request, 'piscineiro/detalhe.html', {'piscineiro': piscineiro})

@login_required
def edit(request, id_piscineiro):
    if not user_is_admin(request.user):
        return HttpResponseForbidden("Acesso restrito a administradores")

    piscineiro = get_object_or_404(Piscineiro, id=id_piscineiro)
    if request.method == 'POST':
        form = PiscineiroForm(request.POST, instance=piscineiro)
        if form.is_valid():
            form.save()
            return redirect('piscineiro_index')
    else:
        form = PiscineiroForm(instance=piscineiro)
    return render(request, 'piscineiro/edit.html', {'form': form, 'piscineiro': piscineiro})

@login_required
def delete(request, id_piscineiro): 
    if not user_is_admin(request.user):
        return HttpResponseForbidden("Acesso restrito a administradores")

    piscineiro = get_object_or_404(Piscineiro, id=id_piscineiro)
    if request.method == 'POST':
        piscineiro.delete()
        return redirect('piscineiro_index')
    return render(request, 'piscineiro/delete.html', {'piscineiro': piscineiro})

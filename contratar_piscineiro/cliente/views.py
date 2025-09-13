from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from contratar_piscineiro.decorators import user_is_admin, user_is_cliente

@login_required
def index(request):
    clientes = Cliente.objects.all()
    
    can_edit = user_is_admin(request.user)
    can_delete = user_is_admin(request.user)
    
    return render(request, 'cliente/index.html', {
        'clientes': clientes,
        'can_edit': can_edit,
        'can_delete': can_delete
    })

@login_required
def add(request):
    if not user_is_cliente(request.user):
        return HttpResponseForbidden("Acesso restrito a clientes")
    
    cliente = get_object_or_404(Cliente, id=request.user.id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            try:
                form.save()
                return redirect('cliente_index')
            except Exception as e:
                form.add_error(None, f'Erro ao salvar: {str(e)}')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente/add.html', {'form': form})

@login_required
def detalhe(request, id_cliente): 
    cliente = get_object_or_404(Cliente, id=id_cliente)
    return render(request, 'cliente/detalhe.html', {'cliente': cliente})


@login_required
def delete(request, id_cliente): 
    if not user_is_admin(request.user):
        return HttpResponseForbidden("Acesso restrito a administradores")

    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_index')
    return render(request, 'cliente/delete.html', {'cliente': cliente})

@login_required
def edit(request, id_cliente):
    if not user_is_admin(request.user):
        return HttpResponseForbidden("Acesso restrito a administradores")

    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_index')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/edit.html', {'form': form, 'cliente': cliente})

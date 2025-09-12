from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name="cliente_index"),
    path('add/', views.add, name="cliente_add"),
    path('delete/<int:id_cliente>/', views.delete, name="cliente_delete"),
    path('<int:id_cliente>/', views.detalhe, name="cliente_detalhe"),
    path('edit/<int:id_cliente>/', views.edit, name="cliente_edit"),
]
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name="manutencao_index"),
    path('add/', views.add, name="manutencao_add"),
    path('delete/<int:id_manutencao>/', views.delete, name="manutencao_delete"),
    path('<int:id_manutencao>/', views.detalhe, name="manutencao_detalhe"),
    path('edit/<int:id_manutencao>/', views.edit, name="manutencao_edit"),
]
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name="equipamento_index"),
    path('add/', views.add, name="equipamento_add"),
    path('delete/<int:id_equipamento>/', views.delete, name="equipamento_delete"),
    path('<int:id_equipamento>/', views.detalhe, name="equipamento_detalhe"),
    path('edit/<int:id_equipamento>/', views.edit, name="equipamento_edit"),
]
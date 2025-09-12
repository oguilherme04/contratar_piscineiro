from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.index, name="piscina_index"),
    path('add/', views.add, name="piscina_add"),
    path('delete/<int:id_piscina>/', views.delete, name="piscina_delete"),
    path('<int:id_piscina>/', views.detalhe, name="piscina_detalhe"),
    path('edit/<int:id_piscina>/', views.edit, name="piscina_edit"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='piscineiro_index'),
    path('add/', views.add, name='piscineiro_add'),
    path('<int:id_piscineiro>/', views.detalhe, name='piscineiro_detail'),
    path('<int:id_piscineiro>/edit/', views.edit, name='piscineiro_edit'),
    path('<int:id_piscineiro>/delete/', views.delete, name='piscineiro_delete'),
]
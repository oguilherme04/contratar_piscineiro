from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="index"),

    path("admin/", admin.site.urls),
    path("piscina/", include("piscina.urls")),
    path("manutencao/", include("manutencao.urls")),
    path("equipamento/", include("equipamento.urls")),
    path("cliente/", include("cliente.urls")),
    path("piscineiro/", include("piscineiro.urls")),
    path('about/', views.about, name="about"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register, name="register"),
]
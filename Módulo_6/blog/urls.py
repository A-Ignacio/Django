from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("quienes-somos/",views.quienesSomos, name="quienes-somos"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("ingreso_usuarios/", views.ingreso_usuarios, name = "ingreso_usuarios")
]

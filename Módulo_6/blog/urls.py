from unicodedata import name
from django import views
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("quienes-somos/",views.quienesSomos, name="quienes-somos"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("ingreso_usuarios/", views.ingreso_usuarios, name = "ingreso_usuarios"),
    path("login", LoginView.as_view(template_name='login.html'), name = 'login'),
    path('salir/', views.logout, name = 'salir'),
    path("salida/", views.salida, name="salida"),
    path('register/', views.register, name='register'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update')
    
]

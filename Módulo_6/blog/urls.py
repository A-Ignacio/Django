from unicodedata import name
from django import views
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("quienes-somos/",views.quienesSomos, name="quienes-somos"),
    path('register/', views.register, name='register'),
    path("login/", LoginView.as_view(template_name='login.html'), name = 'login'),
    path("inicio/", views.iniciologgin, name="iniciologgin"),
    path("quienessomos/",views.quienesSomosR, name="quienes-somosLoggin"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("registrar_libro/", views.registrarLibro, name = "registrar_libro"),
    path('registration/delete/<int:id>', views.deletelibro, name='deletelibro'),
    path('blog/delete/<int:id>', views.deleteUsuario, name='deleteusuario'),
    path("salida/", views.salida, name="salida"),
]

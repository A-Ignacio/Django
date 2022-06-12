from django.shortcuts import render
from .models import Usuario

# Create your views here.

def inicio(request):
    return render (request, "blog/index.html")

def quienesSomos(request):
    return render (request, "blog/quienesSomos.html")

def usuarios(request):
    usuario= Usuario.objects.all()
    return render (request, 'blog/usuarios.html', {"data":usuario})
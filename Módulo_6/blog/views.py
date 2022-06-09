import operator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import User, Libro
from .forms import  UserRegistrationForm, RegistrarLibro
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your views here.

def inicio(request):
    return render (request, "blog/inicio.html")

def quienesSomos(request):
    return render (request, "blog/quienesSomos.html")

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': user_form})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def iniciologgin(request):
    return render (request, "registration/inicio.html")

@login_required
def quienesSomosR(request):
    return render (request, "registration/quienesSomosLoggin.html")

@login_required
@user_passes_test(operator.attrgetter("is_staff"))
def usuarios(request):
    usuario = User.objects.all()
    return render(request, 'blog/usuarios.html', {"data":usuario})

@login_required
def catalogo(request):
    catalogo = Libro.objects.all()
    return render(request, 'blog/catalogo.html', {"data":catalogo})

@login_required
def registrarLibro(request):
    form = RegistrarLibro()
    if request.method == "POST":
            form = RegistrarLibro(request.POST)
            if form.is_valid():
                libro=Libro()
                libro.autor=form.cleaned_data["autor"]
                libro.titulo=form.cleaned_data["titulo"]
                libro.enlace=form.cleaned_data["enlace"]
                libro.save()
                return redirect('catalogo')
            else:
                print("No se ha podido registrar el libro, intente nuevamente")
    return render (request, "registration/registrar_libro.html", {"form":form})

@login_required
def deletelibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return HttpResponseRedirect(reverse('catalogo'))

@login_required
def deleteUsuario(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('usuarios'))


def salida(request):
    return render (request, "blog/salida.html")


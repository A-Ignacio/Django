from multiprocessing import context
import operator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import User, Libro, Comentario
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegisterForm, RegistrarLibro, RegistrarComentario
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.contrib import messages


# Create your views here.

def inicio(request):
    return render (request, "blog/inicio.html")

def quienesSomos(request):
    return render (request, "blog/quienesSomos.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
            

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
                libro.username = request.user
                libro.autor=form.cleaned_data["autor"]
                libro.titulo=form.cleaned_data["titulo"]
                libro.enlace=form.cleaned_data["enlace"]
                libro.save()
                return redirect('catalogo')
            else:
                print("No se ha podido registrar el libro, intente nuevamente")
    return render (request, "registration/registrar_libro.html", {"form":form})

@login_required
def registrarComentario(request):
    form = RegistrarComentario()
    if request.method == "POST":
        form = RegistrarComentario(request.POST)
        if form.is_valid():
            comentario = Comentario()
            comentario.username = request.user
            comentario.titulo = form.cleaned_data["titulo"]
            comentario.contenido = form.cleaned_data["contenido"]
            comentario.save()
            return redirect('comentarios')
        else:
            print("No se ha podido registra el comentario")
    return render(request, "registration/registrar_comentario.html", {"form":form})
        

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

def comentarios(request):
    comentario = Comentario.objects.all()
    return render(request, 'blog/comentarios.html', {"data" : comentario})

def editarComentario(request, id):
    comentario = Comentario.objects.get(pk = id)
    form = RegistrarComentario(instance = comentario)
    if request.method == "POST":
        form = RegistrarComentario(data = request.POST, instance = comentario)
        form.save()
        return redirect('/comentarios')
    else:
        return render (request, 'blog/editar_comentario.html', {"form": form})
    

def eliminarComentario(request, id):
    comentario = Comentario.objects.get(pk = id)
    comentario.delete()
    messages.info(request, 'Comentario eliminado')
    return redirect("/comentarios")

def filtrarComentario(request, username):
    username = Comentario.objects.filter(username = username)
    return render(request, 'blog/filtrar.html', {"username" : username})
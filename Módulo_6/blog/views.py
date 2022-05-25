from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import Usuario, User
from .forms import RegistrarUsuariosForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def inicio(request):
    return render (request, "blog/inicio.html")


def quienesSomos(request):
    return render (request, "blog/quienesSomos.html")

@login_required
def usuarios(request):
    usuario = User.objects.all()
    return render(request, 'blog/usuarios.html', {"data":usuario})
    

def ingreso_usuarios(request):
    form = RegistrarUsuariosForm()
    
    if request.method == "POST":
            form = RegistrarUsuariosForm(request.POST)
            if form.is_valid():
                usuario=Usuario()
                usuario.nombre=form.cleaned_data["nombre"]
                usuario.apellido=form.cleaned_data["apellido"]
                usuario.correo=form.cleaned_data["correo"]
                usuario.telefono=form.cleaned_data["télefono"]
                usuario.ciudad=form.cleaned_data["ciudad"]
                usuario.save()
                return redirect('ingreso_usuarios')
            else:
                print("No se ha podido ingresar el usuario, intente nuevamente")
        
    return render (request, "blog/registrar_usuarios.html", {"form":form})

def logout(request):
    logout(request)
    return redirect('inicio.html')

def salida(request):
    return render (request, "blog/salida.html")

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
    
def delete(request, id):
    user = User.objects.all.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('usuarios'))


def update(request, id):
    user = User.objects.all.get(id=id)
    template = loader.get_template('update.html')
    context = {'user': user,}
    return HttpResponse(template.render(context, request))
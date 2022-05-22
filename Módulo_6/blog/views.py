from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistrarUsuariosForm
# Create your views here.

def inicio(request):
    return render (request, "blog/index.html")

def quienesSomos(request):
    return render (request, "blog/quienesSomos.html")

def usuarios(request):
    usuario= Usuario.objects.all()
    return render (request, 'blog/usuarios.html', {"data":usuario})

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
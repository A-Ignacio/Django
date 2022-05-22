from django import forms 
from django.contrib.auth.models import User  

class RegistrarUsuariosForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required = True)
    apellido = forms.CharField(max_length = 50, required = True)
    correo = forms.CharField(widget = forms.EmailInput)
    télefono = forms.CharField(max_length = 15, required = True)
    ciudad = forms.CharField(max_length = 50, required = True)
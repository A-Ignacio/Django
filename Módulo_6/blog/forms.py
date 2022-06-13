from cProfile import label
from dataclasses import field
from tkinter import Widget
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Libro, Comentario
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    nombreUsuario = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']

class RegistrarLibro(forms.ModelForm):
    autor = forms.CharField(max_length=50, required = True)
    titulo = forms.CharField(max_length=50, required = True)
    enlace = forms.CharField(max_length=100, required = True)
    
    class Meta:
        model = Libro
        fields = ['autor', 'titulo', 'enlace']
    
    
class RegistrarComentario(forms.ModelForm):
    titulo = forms.CharField(label = "Título", max_length=100, required=True)
    contenido = forms.CharField(label = "Comentario", max_length=500, required=True, widget=Textarea)
    
    class Meta:
        model = Comentario
        fields = ['titulo', 'contenido']
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
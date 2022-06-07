from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Libro 

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

class RegistrarLibro(forms.Form):
    autor = forms.CharField(max_length=50, required = True)
    titulo = forms.CharField(max_length=50, required = True)
    enlace = forms.CharField(max_length=100, required = True)

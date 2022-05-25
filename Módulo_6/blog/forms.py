from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User  

class RegistrarUsuariosForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required = True)
    apellido = forms.CharField(max_length = 50, required = True)
    correo = forms.CharField(widget = forms.EmailInput)
    télefono = forms.CharField(max_length = 15, required = True)
    ciudad = forms.CharField(max_length = 50, required = True)
    
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
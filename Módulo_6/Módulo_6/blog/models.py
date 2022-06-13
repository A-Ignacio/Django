from turtle import title, update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre + " " + self.apellido




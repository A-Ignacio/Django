from turtle import title, update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class Libro(models.Model):
    username = models.ForeignKey(User, verbose_name= "Usuario", on_delete=models.DO_NOTHING)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    enlace = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    username = models.ForeignKey(User, verbose_name= "Usuario", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
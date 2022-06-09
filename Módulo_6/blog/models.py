from turtle import title, update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Libro(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    enlace = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

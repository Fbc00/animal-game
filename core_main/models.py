from msilib.schema import Class
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Aposta(models.Model):
    bicho = models.ForeignKey('Bicho', on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resultado = models.BooleanField(default=False)

class Bicho(models.Model):
    nome = models.CharField(
        verbose_name='Nome do Bicho',
        max_length= 32,
    )
    grupo = ArrayField(models.IntegerField())

    
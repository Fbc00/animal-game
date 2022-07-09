from msilib.schema import Class
from pyexpat import model
from django.db import models

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from models import Bicho


# Create your models here.
class Aposta(models.Model):

    bicho_id = models.ForeignKey(Bicho.id)

    data = models.DateField(
        auto_now=True,
    )

    usuario_id = models.ForeignKey(User.id)

    resultado = models.BooleanField(
        default=False,)

class Bicho(models.Model):

    nome = models.CharField(
        verbose_name='Nome do Bicho',
        max_length= 32,
    )

    grupo = ArrayField(models.IntegerField())

    
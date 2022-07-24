
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Aposta(models.Model):
    bicho = models.ForeignKey('Bicho', on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resultado = models.BooleanField(default=False)
    valor = models.FloatField(default=None)
    ganho = models.FloatField(default=0)
    sorteio_aposta = models.ForeignKey('Sorteio', on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    
    def __str__(self):
        return self.data

class Bicho(models.Model):
    nome = models.CharField(
        verbose_name='Nome do Bicho',
        max_length=32,
    )
    url = models.URLField(null=True, blank=True)
    grupo = ArrayField(models.IntegerField(default=list), default=list)
    # grupo = models.CharField(max_length=8, default=list)

    def __str__(self):
        return self.nome


class Sorteio(models.Model):
    data_sorteio = models.DateField(auto_now_add=False, auto_now=False,  null=True, unique=True)
    data_criacao = models.DateField(auto_now_add=True, null=False)
    bicho_sorteado = models.ForeignKey('Bicho', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='bicho_do_dia')
    valido = models.BooleanField(default=True)





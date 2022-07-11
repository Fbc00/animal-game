from django.shortcuts import render
from .models import Bicho, Aposta
# Create your views here.


def index(request):
    aposta = Aposta.objects.all()
    return render(request, 'core/index.html', {'apostas': aposta})


def login(request):
    return render(request, 'core/login.html')


def detalhes(request):
    aposta = Aposta.objects.all()
    return render(request, 'core/detalhes.html', {'apostas': aposta})

def registrar(request):
    return render(request, 'core/registrar.html')
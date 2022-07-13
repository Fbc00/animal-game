import email
from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Bicho, Aposta
from django.contrib.auth.models import User
from django.contrib import messages
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
    if request.method =='POST':

        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)
        senha2 = request.POST.get('senha2',None)

        if senha == senha2:
            if len(senha) >=8 and len(usuario) >=5:
                try:
                    user = User(email = email, username= usuario, password =senha)
                    user.save()

                    messages.success(
                        request,
                        'Visitante Registrado com sucesso !!! logue e se divirta <3'
                    )
                    return redirect('login')
                except IntegrityError as ie:
                    messages.error(
                    request,
                    'Já existe alguem com esse usuario registrado !!!')
                    return redirect('registrar')
            else:
                messages.error(
                    request,
                    'Seu usuario precisa ter 5 digitos ou mais e sua senha precisa de 8 digitos ou mais !!!')

        else:
            messages.error(
                request,
                'Suas senhas estao diferentes !!!')
            return redirect('registrar')
    return render(request, 'core/registrar.html')



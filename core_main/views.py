
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Bicho, Aposta, Sorteio
from datetime import datetime
from django.core.validators import validate_email
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib import messages, auth
# Create your views here.


# @login_required(login_url='login')
# def index(request):
#     aposta = Aposta.objects.filter(id=request.user.id)
#     sorteio = Sorteio.objects.all()
#     # aposta= Aposta.objects.get(bicho=1)
#     return render(request, 'core/index.html', {'objetos': sorteio,'apostas': aposta})

@login_required(login_url='login')
def index(request):
    aposta = Aposta.objects.filter(usuario_id=request.user.id)
    sorteio = Sorteio.objects.all()
    # aposta= Aposta.objects.get(bicho=1)
    return render(request, 'core/index.html', {'objetos': sorteio,'apostas': aposta})
                


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method != 'POST':
        return render(request, 'core/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
        return render(request, 'core/login.html')
    else:
        auth.login(request, user)
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def detalhes(request, id):
    aposta = get_object_or_404(Aposta, id=id)
    bicho = Bicho.objects.all()
    return render(request, 'core/detalhes.html', {'aposta': aposta})


def registrar(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
            messages.error(request, 'Preencha todos os campos')
            return render(request, 'core/registrar.html')
        if senha != senha2:
            messages.error(request, 'Senhas não conferem')
            return render(request, 'core/registrar.html')

        if len(senha) < 6 and len(usuario) < 6:
            messages.error(request, 'Senha ou usuário muito curto')
            return render(request, 'core/registrar.html')

        try:
            validate_email(email)
        except:
            messages.error(request, 'Email inválido')
            return render(request, 'core/registrar.html')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe')
            return render(request, 'core/registrar.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já existe')
            return render(request, 'core/registrar.html')
        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso!')
        user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome,
                                        last_name=sobrenome)
        user.save()
        return redirect('login')
    else:
        return render(request, 'core/registrar.html')

def aposta_feita(request):
    if request.method == 'POST':
        data = request.POST.get('data_valor')
        valor = request.POST.get('valor')
        bichos = request.POST.get('bichos')

        if  not valor.isdigit() and  not (1 >= valor >= 20):
            return redirect('index')

        # if not Sorteio.objects.filter(data_sorteio=data) and not Bicho.objects.filter(id=bichos).exists():
        #     return redirect('index')
        bicho_agora = Bicho.objects.get(id=bichos)
        sorteio_aposta_Agora= Sorteio.objects.get(data_sorteio = data)
        #sorteio_aposta_Agora.strftime("%y/%m/%d")

        aposta = Aposta.objects.create(usuario = request.user, sorteio_aposta = sorteio_aposta_Agora , valor = valor, bicho = bicho_agora)
        aposta.save()
        
    

    return redirect('index')


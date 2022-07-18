import email
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Bicho, Aposta
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.


@login_required(login_url='login')
def index(request):
    aposta = Aposta.objects.filter(id=request.user.id)
    bicho = Bicho.objects.all()
    return render(request, 'core/index.html', {'objetos': bicho, 
                                              'apostas': aposta})


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method != 'POST':
        return render(request, 'core/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'core/login.html')
    else:
        auth.login(request, user)
        # messages.add_message(request, messages.SUCCESS, 'Bem vindo!')
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
    if request.method =='POST':
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)
        senha2 = request.POST.get('senha2',None)

        if senha == senha2:
            user = User(email = email, username= usuario, password =senha)
            user.save()

            messages.success(
                request,
                'Visitante Registrado com sucesso !!! \n logue e se divirta <3'
            )
            return redirect('login')

        else:
            messages.error(
                request,
                'Suas senhas estao diferentes !!!')
            return redirect('registrar')
    return render(request, 'core/registrar.html')




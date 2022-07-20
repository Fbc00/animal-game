import random
from datetime import datetime, timedelta
from core_main.models import Bicho, Aposta, Sorteio
from django.db.models import F

# sortear dois numeros de dois algarismos


def sortear_numeros():
    numero = random.randint(0, 99)
    bichos = Bicho.objects.all()

    for bicho in bichos:
        if numero in bicho.grupo:
            return bicho


def gera_sorteios():
    for i in range(0, 5):
        minha_data = datetime.today().strftime('%d/%m/%Y')
        data = datetime.today().strptime(str(minha_data), "%d/%m/%Y") + timedelta(days=i)
        Sorteio.objects.get_or_create(data_sorteio=data)
    return


def set_sorteio():
    agora = datetime.today().strftime('%d/%m/%Y')
    sorteio = Sorteio.objects.get(data_sorteio=agora).update(bicho_sorteado=sortear_numeros())
    return sorteio


def verifica_se_ganhou():
    data = datetime.today().strftime('%d/%m/%Y')
    sorteio_do_dia = Sorteio.objects.get(data_sorteio=data)
    ganhadores = Aposta.objects.filter(bicho=sorteio_do_dia.bicho_sorteado,
                                       sorteio_aposta=sorteio_do_dia).update(resultado=True, ganho=F('valor') * 18)
    return
# o cara ta realmente fazendo um jogo do bicho com python kkkkkkkkkkkkkkkkkkkk inacreditavelmente foda









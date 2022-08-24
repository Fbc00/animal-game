import random
from datetime import datetime, timedelta
from core_main.models import Bicho, Aposta, Sorteio
from django.db.models import F

# sortear dois numeros de dois algarismos


def sortear_numeros():
    numero = random.randint(0, 26)
    bicho_sorteado = Bicho.objects.get(id=numero)
    return bicho_sorteado

def gera_sorteios():
    for i in range(0, 5):
        minha_data = datetime.today().strftime('%Y-%m-%d')
        data = datetime.today().strptime(str(minha_data), "%Y-%m-%d") + timedelta(days=i)
        Sorteio.objects.get_or_create(data_sorteio=data)
    return


def set_sorteio():
    agora = datetime.today().strftime('%Y-%m-%d')
    bicho = sortear_numeros()
    sorteio = Sorteio.objects.filter(data_sorteio=agora).update(bicho_sorteado_id=bicho.id)
    return


def verifica_se_ganhou():
    data = datetime.today().strftime('%Y-%m-%d')
    data_ganho = datetime.today()
    sorteio_do_dia = Sorteio.objects.get(data_sorteio=data)
    ganhadores = Aposta.objects.filter(bicho_id=sorteio_do_dia.bicho_do_dia.id,
                                       sorteio_aposta_id=sorteio_do_dia.pk).update(resultado=True, ganho=F('valor') * 18)
    return


def desativaSorteio():
    data = datetime.today().strftime('%Y-%m-%d')
    sorteio_do_dia = Sorteio.objects.filter(data_sorteio__lte=data).update(valido=False)
    return
# o cara ta realmente fazendo um jogo do bicho com python kkkkkkkkkkkkkkkkkkkk inacreditavelmente foda









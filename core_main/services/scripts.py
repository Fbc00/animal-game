import random
import datetime
from core_main.models import Bicho, Aposta, Sorteio

# sortear dois numeros de dois algarismos


def sortear_numeros():
    numero = random.randint(0, 99)
    bichos = Bicho.objects.all()

    for bicho in bichos:
        if numero in bicho.grupo:
            return bicho


def gera_sorteio():
    pass


def set_sorteio():
    Sorteio.objects.create(bicho_sorteado=sortear_numeros())
    return


def verifica_se_ganhou():
    data = datetime.datetime.today()
    # UPDATE core_apostas SET resultado = true WHERE bicho_id = oquefoisorteado AND sorteio_data = hoje;

    apostas = Aposta.objects.filter()
    for aposta in apostas:
        if aposta.bicho.grupo == Sorteio.bicho_sorteado.grupo:
            aposta.resultado = True
            aposta.ganho = aposta.valor * 18
            aposta.save()
        else:
            aposta.resultado = False
            aposta.ganho = 0
            aposta.save()






from core_main.models import Aposta
import  datetime

def test_int():
    assert 1==1


def testaUrlAposta(client):
    reposta = client.get('aposta/')
    assert reposta.headers['Content-type'] == "text/html"
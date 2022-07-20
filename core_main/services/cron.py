from core_main.services import scripts


def cron_sorteio_por_semana():
    scripts.gera_sorteios()
    return True


# def my_scheduled_job():
#     scripts.sortear_numeros()
#     scripts.set_sorteio()
#     scripts.verifica_se_ganhou()
#     return True



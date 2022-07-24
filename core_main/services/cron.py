from core_main.services import scripts


def cron_sorteio_por_semana():
    scripts.gera_sorteios()
    return True


def generalJob():
    # scripts.sortear_numeros()
    # scripts.set_sorteio()
    # scripts.verifica_se_ganhou()
    scripts.desativaSorteio()
    return



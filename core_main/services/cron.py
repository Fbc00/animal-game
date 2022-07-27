from core_main.services import scripts
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.scheduled_job('interval', hour=4, timezone="America/Sao_Paulo")
def cron_sorteio_por_semana():
    scripts.desativaSorteio()
    scripts.gera_sorteios()
    return True

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=14, timezone="America/Sao_Paulo")
def generalJob():
    scripts.sortear_numeros()
    scripts.set_sorteio()
    scripts.verifica_se_ganhou()
    return


sched.start()



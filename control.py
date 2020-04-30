from banco_de_dados_ import inserir_dados, criar_banco
from main import get_event_summary, events_future
from tratador_json import take_events, verify_time, summary
import config


plataformas_bet = ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']


def refresh() -> None:
    """Atualiza o banco de dados com os jogos atuais"""

    events_future(1, verify_time())     #atualiza os eventos futuros
    lista = take_events('data/futures_events_.json')  #gera a lista de eventos



    for e in lista[20:]:
        get_event_summary(e.id_event)
        lista = summary('data/summary_event_.json')
        if len(lista) > 0:
            print(lista[0].nome_casa)
            break

refresh()



# --------> Para criar os bancos de dados:
# for plat in plataformas_bet:
#     criar_banco(f'json_files/{plat}/banco_{plat}_future.bd')

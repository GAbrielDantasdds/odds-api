from banco_de_dados_ import inserir_dados
from main import get_event_odds, events_future
from tratador_json import take_events, verify_time
import config.config


plataformas_bet = ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']


def refresh() -> None:
    """Atualiza o banco de dados com os jogos atuais"""

    events_future(1, verify_time())     #atualiza os eventos futuros
    lista = take_events('data/futures_events_.json')  #gera a lista de eventos


    for event in lista:
        for plataforma in plataformas_bet:
            print(event.id_event)
            get_event_odds(event.id_event, plataforma)

        break



refresh()

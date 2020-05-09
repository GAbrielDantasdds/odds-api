from app.control.banco_de_dados_ import inserir_dados, criar_banco, banco_eventos_futuros_atualizar, banco_odds_atualizar, insert_id
from app.control.main import get_event_summary, events_future
from app.control.tratador_json import take_events, verify_time, summary
from app.control.tratar_banco import get_events_id_from_db
import app.config


def odds_to_bd(sport: str) -> None:
    """ Adiciona as cotações em um banco de dados. """

    lista_de_id = get_events_id_from_db(sport, verify_time())
    sport_id = app.config.sports()

    for id in lista_de_id:
        get_event_summary(id[0])
        lista_cotacoes = summary(r'app/data/summary_event_.json', sport_id[sport])
        banco_odds_atualizar(sport, lista_cotacoes, id[0])


def refresh(sport: str) -> None:
    """ Atualiza o banco de dados com os jogos atuais. """

    dic = app.config.sports()
    print(dic[sport])
    page_count = 1
    print('Pegando eventos de ', sport)
    while events_future(dic[sport], verify_time(), page=page_count):          #atualiza os eventos futuros
        lista_de_eventos = take_events('app/data/futures_events_.json')       #gera a lista de eventos
        banco_eventos_futuros_atualizar(lista_de_eventos, sport)
        page_count += 1

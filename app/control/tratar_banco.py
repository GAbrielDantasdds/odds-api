from app.control.banco_de_dados_ import criar_
from app.control.tratador_json import verify_time
import sqlite3 as sq


def get_events_id_from_db(sport: str, time: str) -> list:
    """ Obtém os dados dos eventos e suas respectivas odds. """

    cursor_eventos = criar_(f'app/models/bd/events/{sport}_em_analise{time}.db')[0]
    cursor_eventos.execute('''SELECT event_id FROM data''')
    lista_de_eventos_by_id = cursor_eventos.fetchall()
    return lista_de_eventos_by_id


def take_league(sport: str) -> list:
    """ Retorna todas as ligas de determinado esporte. """

    cursor = criar_(f'app/models/bd/events/{sport}_em_analise{20200506}.db')[0] #verify_time()
    cursor.execute('''SELECT event_league FROM data group by event_league''')
    _list = cursor.fetchall()
    _list = [x[0] for x in _list]
    return _list

def take_events_name(event_league: str, sport: str) -> list:
    """ Retorna os jogos pelos eventos. """

    cursor = criar_(f'app/models/bd/events/{sport}_em_analise{20200506}.db')[0]
    cursor.execute('''SELECT event_name, event_id FROM data WHERE event_league == ?''', [event_league])

    lista_de_eventos_by_name = cursor.fetchall()
    return lista_de_eventos_by_name


def take_odds(id: str, sport: str) -> list:
    """ Retorna as cotações por id do evento. """

    cursor = criar_(f'app/models/bd/odds/{sport}_odds_{20200506}.db')[0]
    cursor.execute('''SELECT bet_name, home_od, draw_od, away_od FROM data WHERE event_id == ?''', [id])

    _lista = cursor.fetchall()
    return _lista

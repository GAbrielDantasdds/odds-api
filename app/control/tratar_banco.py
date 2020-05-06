from app.control.banco_de_dados_ import criar_
import sqlite3 as sq


def get_events_id_from_db(sport: str, time: str) -> list:
    """ Obtém os dados dos eventos e suas respectivas odds. """

    cursor_eventos = criar_(f'app/models/bd/events/{sport}_em_analise{time}.db')[0]
    cursor_eventos.execute('''SELECT event_id FROM data''')
    lista_de_eventos_by_id = cursor_eventos.fetchall()
    return lista_de_eventos_by_id

    # cursor_odds = criar_(r'bd/odds/odds_.json.bd')[0]
    # for ide in lista_de_eventos_by_id:
    #     cursor_odds.execute('''SELECT NAME_BET, HOME_OD, DRAW_OD, AWAY_OD FROM data WHERE ID == ?''', [ide[0]])
    #     print(cursor_odds.fetchall())

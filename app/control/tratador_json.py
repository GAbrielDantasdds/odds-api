import json
import calendar, time
from app.config import plataformas


class league():
    """liga dos eventos"""

    def __init__(self, id_league: int, name: str, cc: str):
        self.id_league = id_league
        self.name = name
        self.cc = cc

class team():
    """Os times que estão jogando."""

    def __init__(self, id_team: int, name: str, cc: str):
        self.id_team = id_team
        self.name = name
        self.cc = cc


class evento():
    """Classe dos eventos"""

    def __init__(self, id_event: int, sport_id: int, data: int, status: int, _league: league, _home: team, _away: team):
        self.id_event= id_event
        self.sport_id = sport_id
        self.data = data
        self.status = status
        self.league = league(_league['id'], _league['name'], _league['cc'])
        self.home = team(_home['id'], _home['name'], _home['cc'])
        self.away = team(_away['id'], _away['name'], _away['cc'])
        self.cotacao = None

    def add_odd(self, cot: dict) -> None:
        self.cotacao = cot


class odd():
    """ Cotações dos eventos. """

    def __init__(self, nome_casa: str, mkt_1_1: list):
        self.nome_casa = nome_casa
        self.mkt_1_1 = mkt_1_1



def json_to_dic(nome_arquivo: str) -> dict:
    """" Converte os arquivos json para dict. """

    with open(nome_arquivo, 'r') as arquivo:
        data = arquivo.readline()
        arquivo.close()
        return json.loads(data)


def take_events(nome_arquivo: str) -> list:
    """ Pega os valores do arquivo JSON e transforma em uma lista de classes. """

    data = json_to_dic(nome_arquivo)
    event_list = []
    response = data['results']
    for e in response:
        event_list.append(evento(e['id'], e['sport_id'], e['time'], e['time_status'], e['league'], e['home'], e['away']))
    return event_list

def verify_time() -> int:
    """ Retorna o próximo dia. """

    return time.strftime("%Y%m%d", time.localtime(time.time() + 86000))



def tratar_odds(nome_arquivo: str, source='bet365') -> list:
    """ Trata as cotações de cada envento que recebe. """

    data = json_to_dic(f'json_files/{source}/{nome_arquivo}')
    response = data['results']['odds']
    print(response)


def events_futures_(nome_arquivo: str) -> list: # <-------------------------- v.2.0
    """ Trata os eventos futuros. """

    data = json_to_dic(nome_arquivo)
    response = data['results']
    events = []

    for r in response:
        _novo_evento = evento(r['id'], r['sport_id'], r['time'], r['time_status'], r['league'], r['home'], r['away'])
        events.append(_novo_evento)
    return events



def summary(nome_arquivo: str, sport_id) -> list:
    """ Pega o json com os sumários e transforma em objeto. """

    data = json_to_dic(nome_arquivo)
    response = data['results']
    if response == None:
        return []
    lista_cot = []
    plataformas_ = plataformas()

    for name, results in response.items():
        if name.lower() in plataformas_:
            if sport_id == 1:
                if results['odds']['start'][f'{sport_id}_1'] != None:
                    _1_1 = [results['odds']['start'][f'{sport_id}_1']['home_od'],
                            results['odds']['start'][f'{sport_id}_1']['draw_od'],
                            results['odds']['start'][f'{sport_id}_1']['away_od']]
                else:
                    _1_1 = None
            else:
                if results['odds']['start'][f'{sport_id}_1'] != None:
                    _1_1 = [results['odds']['start'][f'{sport_id}_1']['home_od'],
                            None,
                            results['odds']['start'][f'{sport_id}_1']['away_od'],]
                else:
                    _1_1 = None

            _cotacao = odd(name, _1_1)
            lista_cot.append(_cotacao)

    return lista_cot

# ------------- ODDS API ----------------------------------

def tratar_odds_2(nome_arquivo: str) -> dict:
    data = json_to_dic(nome_arquivo)
    lista_de_eventos = []

    class cotacao():
        def __init__(self, mkt: str, home:str, away:str, odds: dict):
            self.mkt = mkt
            self.home = home
            self.away = away
            self.home_od = odds['h2h']
            self.away_od = odds['h2h']
            if len(odds) > 2:
                self.draw_od = odds[2]

    class event():
        def __init__(self, name: str, time: int, sites: list, cot: cotacao):
            self.name = name
            self.time = time
            self.sites = sites
            self.cotacao = _cot

    for evento in data['data']:
        _cot = cotacao(evento['sites'] , evento['teams'][0], evento['teams'][1], evento['sites'][0]['odds'])
        _evento = event(evento['sport_nice'], evento['commence_time'], evento['sites'], _cot)
        lista_de_eventos.append(_evento)

    return lista_de_eventos






# ---------------------------------------------------------

import requests as r
from config import api_key
import json
import os

token = '46686-aMprSfbKrPfl2i'
headers = {'Content-Type': 'application/json',
'X-API-TOKEN': '{0}'.format(token)}


# - Nome time1.  # home
# - Nome time2.  # away
#
# -Hora.         #time
# -Data.
#
# ODDS:
# - time 1 ganhando.  # home_od
# - time 2 ganhando.  # away_od
# - dupla hipótese: time 1 ganhando ou empate.
# - dupla hipótese: time 2 ganhando ou empate.


# -------------------- ODDS API ---------------------------

def get_odds_(sport_: str, region_: str, mkt_: str) -> dict:
    """Retorna os odds dos próximos jogos"""

    api_ = api_key()
    params = {'api_key': api_, 'sport': sport_, 'region': region_, 'mkt': mkt_}

    response = r.get('https://api.the-odds-api.com/v3/odds', params=params)
    odds_json = json.loads(response.text)

    if not odds_json['success']:
        raise odds_json['msg']

    with open('teste.json', 'w') as target:
        target.write(f'{response.text}')
    print(response.headers['x-requests-remaining'])
    return odds_json

get_odds_('upcoming', 'eu', 'h2h')


# ----------------------------------------------------------


def get_event_history(event_id: int, source='bet365') -> None:
    """Histórico de eventos"""

    url = f'https://api.betsapi.com/v1/event/history?&event_id={event_id}?source={source}'
    re = r.get(url, headers=headers)
    if re.status_code == 200:
        with open(f'json_files/{source}/ended_events_.json', 'w') as arquivo:
            arquivo.write(f'{re.content.decode("UTF-8")}')

def get_event_odds(event_id: int, source='bet365') -> None:
    """Pega os odds de eventos"""

    url = f'https://api.betsapi.com/v2/event/odds?&event_id={event_id}&source={source}'
    re = r.get(url, headers=headers)
    if re.status_code == 200:
        with open(f'json_files/{source}/{source}_odds_events_.json', 'w') as arquivo:
            arquivo.write(f'{re.content.decode("UTF-8")}')

def events_future(id: int, data: int, source='bet365') -> None:
    """Vê os eventos futuros por esporte"""

    _url = f'https://api.betsapi.com/v2/events/upcoming?sport_id={id}&source={source}&day={data}'
    re = r.get(_url, headers=headers)
    if re.status_code == 200:
        with open(f'data/futures_events_.json', 'w') as arquivo:
            arquivo.write(f'{re.content.decode("UTF-8")}')

def events_inplay(id: int, source='1xbet') -> None:
    """Eventos ocorrendo em tempo real"""

    _url = f'https://api.betsapi.com/v2/events/inplay?sport_id={id}?cc=br?source={source}?page=3'
    re = r.get(_url, headers=headers)
    if re.status_code == 200:
        with open(f'data/inplay_events{id}_.json', 'w') as arquivo:
            arquivo.write(f'{re.content.decode("UTF-8")}')
    elif re.status_code == 500:
        print('Erro no servidor BET, contate o suporte.')
    elif re.status_code == 404:
        print('Não foram encotrado dados')

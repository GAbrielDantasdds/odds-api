from glob import glob
from json import loads, dumps
from getpass import getpass
import os


def api_key():
    return 'your-token'

def plataformas():
    return ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']

def plataformas_dic():
    return {'Bet365': 0, '188bet': 1, 'Vbet': 2, 'Betway': 3, 'Pinnacle': 4, '1XBet': 5}

def sports():
    return {'soccer': 1, 'table_tenis': 92, 'volleyball': 91, 'tennis': 13}

def verify(time: str) -> list:
    """ verifica se o arquivo existe. """

    var  = time
    base = 'app/models\\bd\\events\\'
    base_odds = 'app/models\\bd\\odds\\'
    fouds = []

    dic = {'soccer':      f'{base}soccer_em_analise{var}.db',
           'tennis':      f'{base}tennis_em_analise{var}.db',
           'table_tenis': f'{base}table_tenis_em_analise{var}.db',
           'volleyball':  f'{base}volleyball_em_analise{var}.db'}

    arquivos = glob(base + '*db')
    for arquivo in arquivos:
        for sport in dic:
            if sport in arquivo:
                if var in arquivo:
                    fouds.append(True)
    if len(fouds) == 0:
        for arquivo in arquivos:
            os.remove(arquivo)
        for arquivo in glob(base_odds + '*db'):
            os.remove(arquivo)
        return False
    else:
        return True


class user():
    def __init__(self, nome):
        self.nome = nome

class infos():
    def __init__(self):
        pass

    def data(self):
        with open(r'app/config/infos.json', 'r') as file:
            _data = loads(file.readline())
        return _data

    def criar_infos(self, serial_key, user):
        with open(r'app/config/infos.json', 'w') as file:
            _dic = {'infos': {'key': serial_key}, 'user': user.nome}
            file.write(f'{dumps(_dic)}')


    def get_key(self):
        _data = self.data()
        return _data['infos']['key']

    def get_user(self):
        _data = self.data()
        return _data['user']

    def insert_info(self, key, value):
        _data = self.data()
        _data[key] = value
        with open(r'app/config/infos.json', 'w') as file:
            file.write(f'{dumps(_data)}')

    def get_info(self, key):
        return self.data()[key]


def take_data():
    _nome = input('Digite seu nome: ')
    _key  = getpass('Digite uma senha: ')
    _user = user(_nome)
    _novas_infos = infos()
    _novas_infos.criar_infos(_key, _user)



def acesso():
    if len(glob('app/config/*json')) == 0:
        take_data()
        return False
    else:
        return True

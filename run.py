from app.control.control import refresh, odds_to_bd
from app.control.banco_de_dados_ import banco_eventos_futuros
from app.control.tratador_json import verify_time
from app.config import sports, verify, acesso, infos

# UI
from app.templates.call import iniciar
from app.templates.table import chamar_tabela, _main
from app.templates._main import *

# QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
import sys
import os

from time import sleep
from getpass import getpass
from threading import Thread


def start() -> None:
    """ Inicia o loop para pegar os eventos e suas casas. """

    info = infos()
    sleep_time = 10  #info.get_info('sleep_time')

    data = verify(verify_time())
    if data:
        info.insert_info('status', 'running')
        while info.get_info('status') == 'running':
            print('+ Atualizando...')
            for sport in sports():
                if sport != 'soccer':
                    refresh(sport)
                    odds_to_bd(sport)
            _main.busca_dados()
            print('+ Eventos atualizados!')
            sleep(sleep_time)
    else:
        for sport in sports():
            banco_eventos_futuros(sport)
        start()

def limpa() -> None:
    """ Limpa a tela do console. Somente em Windows """

    os.system('cls')

def autenticar():
    if acesso() == True:
        _pass = getpass('+ Senha: ')
        _infos = infos()
        if _pass == _infos.get_key():
            limpa()
            print(f'\nSeja bem vindo, {_infos.get_user()}\n')
            menu()
        else:
            print('+ Senha incorreta!')
            sleep(2)
            limpa()
            autenticar()


def menu():

    def sair():
        info = infos()
        info.insert_info('status', 'stoped')
        return False

    opcoes = {'1': iniciar, '2': chamar_tabela, '3': start, '4': sair}

    def mostra_opcoes():
        print('++++++++++++++ _ODDS BOT_ ++++++++++++++\n')
        print('[1] Painel visualização Individual\n[2] Painel visualização por Liga')
        print('[3] Iniciar requisições\n[4] Sair')

    mostra_opcoes()
    _res = input()
    try:
        _new_thread = Thread(name=f'{opcoes[_res]}', target=opcoes[_res])
        _new_thread.start()
        while _res in opcoes.keys():
            limpa()
            menu()
    except KeyError:
        print('+ Opção inválida!')
        sleep(2)
        limpa()
        menu()

if __name__ == '__main__':
    autenticar()

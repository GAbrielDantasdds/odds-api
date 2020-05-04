# import app.control.main
from app.control.control import refresh
from time import sleep



def start():
    sports = {'soccer': 1, 'table_tenis': 92, 'volleyball': 91,
              'tennis': 13}

    for i in range(1):
        for sport in sports:
            refresh(int(sports[sport]))
            print(f'Odds de {sport} atualizados!')
        print('Proxima atalização em 10 minutos.')

start()

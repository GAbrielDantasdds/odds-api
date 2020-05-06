from app.control.control import refresh, odds_to_bd
from app.control.banco_de_dados_ import banco_eventos_futuros
from app.control.tratador_json import verify_time
from time import sleep
from app.config import sports, verify


def start() -> None:
    """ Inicia o loop para pegar os eventos e suas casas. """

    data = verify(verify_time())

    if (True in data):
        for sport in sports():
            # refresh(sport)
            odds_to_bd(sport)
    else:
        for sport in sports():
            banco_eventos_futuros(sport)
        start()


start()
print('Done!')

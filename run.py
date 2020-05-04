from app.control.control import refresh
from time import sleep
from app.config import sports


def start():
    """ Inicia o loop para pegar os eventos e suas casas. """

    for i in range(10):
        refresh(sports())
        break

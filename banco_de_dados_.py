import sqlite3 as sq
from tratador_json import verify_time, tratar_odds_2

def criar_(nome: str) -> list:
    """ Cria uma instância da conexão e cursor """

    conexao = sq.connect(nome)
    return conexao.cursor(), conexao

def criar_banco(nome_banco: str) -> None:
    """ Cria um novo banco de dados. """

    cursor = criar_(f'{nome_banco}.bd')[0]
    cursor.execute('''CREATE TABLE IF NOT EXISTS data('ID', 'NAME_BET', 'HOME_OD', 'DRAW_OD', 'AWAY_OD')''')

def inserir_dados(nome_banco: str, data: list, tp: bool) -> None:
    """ Insere dados no banco selecionado. """

    cursor, conexao = criar_(f'{nome_banco}.bd')

    # inserindo dados no banco eventos
    if tp:
        cursor.execute('''INSERT INTO data('ID', 'SPORT_ID', 'LEAGUE', 'TIME', 'HOME_NAME', 'AWAY_NAME') values(?,?,?,?,?,?)''',
        data)
    else:
        cursor.execute('''INSERT INTO data('ID', 'NAME_BET', 'HOME_OD', 'DRAW_OD', 'AWAY_OD') values(?,?,?,?,?)''',
        data)

    conexao.commit()

def banco_eventos_futuros() -> None:
    """ Banco de dados que vai receber os eventos que ocorrerão em 24hrs. """

    cursor, conexao = criar_(f'eventos_dia_{verify_time()}.db')
    cursor.execute('''CREATE TABLE IF NOT EXISTS data(event_id, event_name, event_time)''')

def banco_eventos_futuros_atualizar(eventos: list) -> None:
    """ Insere dados de eventos futuros. """

    banco_eventos_futuros()
    cursor, conexao = criar_(f'eventos_dia_{verify_time()}.db')
    for e in eventos:
        cursor.execute('''INSERT INTO data(event_id, event_name, event_time) values(?,?,?)''', [e.name, f'{e.cotacao.home} x {e.cotacao.away}', e.time])
    conexao.commit()

criar_banco(r'bd/odds/odds_.json')

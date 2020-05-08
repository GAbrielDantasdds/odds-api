import sqlite3 as sq
from app.control.tratador_json import verify_time, tratar_odds_2


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


def banco_eventos_futuros(sport) -> None:
    """ Banco de dados que vai receber os eventos que ocorrerão em 24hrs. """

    cursor, conexao = criar_(f'app/models/bd/events/{sport}_em_analise{verify_time()}.db')
    cursor.execute('''CREATE TABLE IF NOT EXISTS data(event_id, event_name, event_league, event_time)''')

    cursor, conexao = criar_(f'app/models/bd/odds/{sport}_odds_{verify_time()}.db')
    cursor.execute('''CREATE TABLE IF NOT EXISTS data(event_id, bet_name, home_od, draw_od, away_od)''')



def insert_id(lista: list, sport: str) -> None:
    """ Insere o id no banco das cotações. """

    cursor, conexao = criar_(f'app/models/bd/odds/{sport}_odds_{verify_time()}.db')

    for evento in lista:
        cursor.execute('''INSERT INTO data(event_id) values(?)''', [evento.id_event])
    conexao.commit()



def banco_eventos_futuros_atualizar(eventos: list, sport: str) -> None:
    """ Insere dados de eventos futuros. """

    insert_id(eventos, sport)
    cursor, conexao = criar_(f'app/models/bd/events/{sport}_em_analise{verify_time()}.db')
    for e in eventos:
        cursor.execute('''INSERT INTO data(event_id, event_name, event_league, event_time) values(?,?,?,?)''', [e.id_event, f'{e.home.name} x {e.away.name}', e.league.name, e.data])
    conexao.commit()


def banco_odds_atualizar(sport: str, lista_de_odds: list, id: int) -> None:
    """ Insere as cotações no banco de dados. """

    cursor, conexao = criar_(f'app/models/bd/odds/{sport}_odds_{verify_time()}.db')
    sport = str(sport)

    for odd in lista_de_odds:
        if odd.mkt_1_1 != None:
            try:
                cursor.execute('''UPDATE data set bet_name = ?, home_od = ?, draw_od = ?, away_od = ? WHERE event_id == ?''',
                [odd.nome_casa, odd.mkt_1_1[0], odd.mkt_1_1[1], odd.mkt_1_1[2], id])
                conexao.commit()
            except Exception as e:
                print(e)

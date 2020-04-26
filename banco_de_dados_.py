import sqlite3 as sq


def criar_banco(nome_banco: str) -> None:
    '''Cria um novo banco de dados'''
    conexao = sq.connect(f'{nome_banco}.bd')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data('Time 1', 'Time 2', Data, Hora, 'Time 1 ganhando', Empate, 'Time 2 ganhando',
    'Time 1 ganha ou empate', 'Time 2 ganha ou empate')''')

def inserir_dados(nome_banco: str) -> None:
    '''Insere dados no banco selecionado'''
    conexao = sq.connect(f'{nome_banco}.bd')
    cursor = conexao.cursor()

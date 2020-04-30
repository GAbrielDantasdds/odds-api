from banco_de_dados_ import inserir_dados, criar_banco
from main import get_event_summary, events_future
from tratador_json import take_events, verify_time, summary
import config


plataformas_bet = ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']


def refresh() -> None:
    """ Atualiza o banco de dados com os jogos atuais. """

    events_future(1, verify_time())     #atualiza os eventos futuros
    lista_de_eventos = take_events('data/futures_events_.json')  #gera a lista de eventos



    for e in lista_de_eventos:
        if 'Esoccer' not in e.league.name:
            get_event_summary(e.id_event)
            lista_cotacoes = summary('data/summary_event_.json')
            if len(lista_cotacoes) < 2:
                pass                     #add a lista de verificaçao pra ver mais tarde
            else:
                print()
                print('Casas e suas cotações para: ', e.home.name, ' vs ', e.away.name)
                for cot in lista_cotacoes:
                    print(cot.nome_casa, ' Time 1 ganhar: ', cot.mkt_1_1[0], ' ', ' Time 2 ganhar: ', cot.mkt_1_1[1])

        else:
            pass

refresh()



# --------> Para criar os bancos de dados:
# for plat in plataformas_bet:
#     criar_banco(f'json_files/{plat}/banco_{plat}_future.bd')

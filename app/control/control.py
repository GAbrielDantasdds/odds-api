from app.control.banco_de_dados_ import inserir_dados, criar_banco
from app.control.main import get_event_summary, events_future
from app.control.tratador_json import take_events, verify_time, summary
import app.config


plataformas_bet = ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']

def refresh(sport) -> None:
    """ Atualiza o banco de dados com os jogos atuais. """

    page_count = 1
    print('Pegando evento')
    while events_future(sport, verify_time(), page=page_count):     #atualiza os eventos futuros
        lista_de_eventos = take_events('app/data/futures_events_.json')  #gera a lista de eventos

        print('Iterenado eventos')
        for e in lista_de_eventos:
            if 'Esoccer' not in e.league.name:
                get_event_summary(e.id_event)
                lista_cotacoes = summary(r'app/data/summary_event_.json', sport)
                print('Cotações: ', lista_cotacoes)
                print('Casas e suas cotações para: ', e.home.name, ' vs ', e.away.name)
                inserir_dados(r'app/models/bd/events/eventos_.json', [e.id_event, e.sport_id, e.league.name,
                                                             e.data, e.home.name,e.away.name], True)
                for cot in lista_cotacoes:
                    print(cot)
                    if sport == 1:
                        print(cot.nome_casa, ' Time 1 ganhar: ', cot.mkt_1_1[0], ' ', ' Time 2 ganhar: ', cot.mkt_1_1[2])
                        inserir_dados(r'app/models/bd/odds/odds_.json', [e.id_event, cot.nome_casa, cot.mkt_1_1[0], cot.mkt_1_1[1], cot.mkt_1_1[2]], False)
                    else:
                        print(cot.nome_casa, ' Time 1 ganhar: ', cot.mkt_1_1[0], ' ', ' Time 2 ganhar: ', cot.mkt_1_1[1])
                        inserir_dados(r'app/models/bd/odds/odds_.json', [e.id_event, cot.nome_casa, cot.mkt_1_1[0], None, cot.mkt_1_1[1]], False)


            else:
                pass
        page_count += 1


# --------> Para criar os bancos de dados:
# for plat in plataformas_bet:
#     criar_banco(f'json_files/{plat}/banco_{plat}_future.bd')

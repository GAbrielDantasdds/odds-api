from app.control.banco_de_dados_ import inserir_dados, criar_banco
from app.control.main import get_event_summary, events_future
from app.control.tratador_json import take_events, verify_time, summary
import app.config


plataformas_bet = ['1xbet', '188bet', 'bet365', 'betway', 'pinnaclesports', 'vbet']

def refresh() -> None:
    """ Atualiza o banco de dados com os jogos atuais. """

    events_future(1, verify_time())     #atualiza os eventos futuros
    lista_de_eventos = take_events('data/futures_events_.json')  #gera a lista de eventos


    print('Carregando...')
    for e in lista_de_eventos:
        if 'Esoccer' not in e.league.name:
            get_event_summary(e.id_event)
            lista_cotacoes = summary(r'app/data/summary_event_.json')
            if len(lista_cotacoes) < 2:
                pass                     #add a lista de verificaçao pra ver mais tarde
            else:
                print('Casas e suas cotações para: ', e.home.name, ' vs ', e.away.name)
                inserir_dados(r'app/models/bd/events/eventos_.json', [e.id_event, e.sport_id, e.league.name,
                                                             e.data, e.home.name,e.away.name], True)
                for cot in lista_cotacoes:
                    print(cot.nome_casa, ' Time 1 ganhar: ', cot.mkt_1_1[0], ' ', ' Time 2 ganhar: ', cot.mkt_1_1[2])
                    inserir_dados(r'app/models/bd/odds/odds_.json', [e.id_event, cot.nome_casa, cot.mkt_1_1[0], cot.mkt_1_1[1], cot.mkt_1_1[2]], False)


        else:
            pass
    print('Concluido!')

refresh()



# --------> Para criar os bancos de dados:
# for plat in plataformas_bet:
#     criar_banco(f'json_files/{plat}/banco_{plat}_future.bd')

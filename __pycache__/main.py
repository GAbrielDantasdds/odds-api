from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver as d
from math import trunc
from time import sleep
import os

def rodar() -> None:
    '''Inicia o progarma'''

    _url = 'https://www.bet365.com/#/IP/'
    navegador = d.Chrome(r'C:\Users\usuario\Desktop\chromedriver.exe')
    navegador.get(_url)


    def get_data() -> dict:
        '''Tenta captar o nome e score dos players'''
        _name1 = navegador.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div[1]')
        _name2 = navegador.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div[3]/div[2]')
        _score1 = navegador.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]')
        _score2 = navegador.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div[3]/div[1]')
        return {'Jogador 1': _name1.text, 'Score 1': _score1.text, 'Jogador 2': _name2.text, 'Score 2': _score2.text}


    def placar(dic: dict) -> None:
        '''Mostra o placar de maneira elegante'''
        print('--------------------# PLACAR #---------------------\n')
        print(dic['Jogador 1'], ' vs ', dic['Jogador 2'])
        _len1 = trunc((len(dic['Jogador 1']))/2)
        _len2 = trunc((len(dic['Jogador 2']))/2)

        print(_len1 * ' ' + dic['Score 1'] + ((_len1 - 1)* ' '), end=f"{_len2 * ' '}")
        print( + dic['Score 2'] + ((_len2 - 1)* ' '))



    def ir_para_pagina_tenis():
        # IR PARA A PAG AO VIVO:
        botao_ao_vivo = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]")))
        botao_ao_vivo.click() # CLICANDO NO BOTÃO

        # IR PARA A ABA TÊNIS:
        botao_tenis = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "ipo-ClassificationBarButtonBase ipo-ClassificationBarButtonBase_Selected ipo-ClassificationBarButtonBase_Selected-13 ")))
        botao_tenis.click()

    ir_para_pagina_tenis()
    sleep(20)




rodar()

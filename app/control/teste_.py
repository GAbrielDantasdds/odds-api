from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs

from selenium.webdriver.chrome.options import Options
from selenium import webdriver as d
from time import sleep

import sys

link = 'https://www.bet365.com/#/AC/B1/C1/D8/E88778349/F3/P^13/Q^48633251'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#
# pag = Request(link, headers=headers)
#
# html = urlopen(pag).read()
#
# soup = bs(html, 'html.parser')
#
# print(soup.pretiffy())

chrome_option = Options()
chrome_option.add_argument('--headless')
# chrome_option.add_argument(headers)

path = r'C:\Users\usuario\Desktop\chromedriver.exe'

nav = d.Chrome(path)



nav.get(link)

for i in range(20):
    print('Carregando...')
    sleep(1)

grupos = nav.find_elements_by_class_name('gl-Participant_Odds')
for grupo in grupos:
    print(grupo.text)

c = input('Fim.')
# soup = bs(nav.page_source, 'html.parser')
#
# for  p in soup.find_all(class_='bookies bk_betfair'):
#     print(p.text)

print('Rodando...........--------------')

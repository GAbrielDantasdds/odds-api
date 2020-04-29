from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs

from selenium.webdriver.chrome.options import Options
from selenium import webdriver as d
from time import sleep

link = 'https://oddspedia.com/br/futebol/bielorrussia/copa-da-bielorrussia/shakhtyor-soligorsk-dinamo-brest-3961641/'

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#
# pag = Request(link, headers=headers)
#
# html = urlopen(pag).read()
#
# soup = bs(html, 'html.parser')
#
# print(soup.find_all('odd-link-wrapper'))

chrome_option = Options()
chrome_option.add_argument('--headless')

path = r'C:\Users\usuario\Desktop\chromedriver.exe'

nav = d.Chrome(path, options=chrome_option)



nav.get(link)

for i in range(5):
    print('Carregando...')
    sleep(1)

linhas = nav.find_elements_by_class_name('movement-wrapper have-moves w-100')
for linha in linha:
    print(nome.text)

soup = bs(nav.page_source, 'html.parser')

for  p in soup.find_all(class_='bookies bk_betfair'):
    print(p.text)

import requests
from bs4 import BeautifulSoup

page = requests.get("https://pt.wikipedia.org/wiki/Lista_de_c%C3%B3digos_de_estado_HTTP")
soup = BeautifulSoup(page.content, 'html.parser')

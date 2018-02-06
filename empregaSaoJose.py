import requests

from bs4 import BeautifulSoup

page = requests.get("https://www.empregasaojosecampos.com")
soup = BeautifulSoup(page.content, 'html.parser')

[print (item.getText()) for item in list(soup.findAll("span", {"itemprop": "title"}))] #Ultimas vagas de empregos
nomeDaVaga = soup.find("span", {"itemprop": "title"})
enunciados = soup.find("div", {"class": "content-area col-sm-12 col-md-8"})

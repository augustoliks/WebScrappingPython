import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.empregasaojosecampos.com")
soup = BeautifulSoup(page.content, 'html.parser')

enunciados = soup.findAll("div", class_="blog-post")

vaga = enunciados[0]

headerVaga = vaga.find("span", class_="blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga

dados = vaga.find("div", class_="metadata")

dataVaga = dados.find("time", class_="value-title").getText()

caracteristicas = dados.findAll("span")

cidade = caracteristicas[2]
estado = caracteristicas[3]
pais = caracteristicas[4]
salario = caracteristicas[5]
nivelAcademico = caracteristicas[7]
statusVaga = caracteristicas[8]
tempoContrato = caracteristicas[9]

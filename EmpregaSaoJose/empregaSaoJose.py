import requests
import json
from bs4 import BeautifulSoup
from time import sleep
import datetime

urlBase = "https://www.empregasaojosecampos.com"

def make_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def calcular_data(data):
    dataPublicacao = datetime.date(day = int( data[0:2] ), month = int( data[3:5] ), year = int( data[-4:] ) )
    hoje = datetime.date.today()
    return (hoje - dataPublicacao).days

def empregos_api(url):
    soup = make_soup(url)
    lista_vagas = soup.findAll("div", class_="blog-post")
    k = 0
    while(k <= len(lista_vagas[:-1]) ) :
        headerVaga = lista_vagas[k].find("span", class_="blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga
        dadosVaga = lista_vagas[k].find("div", class_="metadata")
        caracteristicas = dadosVaga.findAll("span")
        nomeVaga = headerVaga.getText()[1:-1]
        data = dadosVaga.find("time", class_="value-title").getText()[-10:]

        print ( {
                'nomeVaga': nomeVaga,
                'local': caracteristicas[2].getText() + ', ' + caracteristicas[3].getText() + ' - ' + caracteristicas[4].getText(),
                'data': data,
                'diffData': calcular_data(data),
                'linkVaga': headerVaga.find("a").get("href"),
                'salario': caracteristicas[5].getText(),
                'nivelAcademico': caracteristicas[7].getText(),
                'statusVaga': caracteristicas[8].getText()
            }  )

        print("\n\n")
        k+=1
        sleep(2)

def pes_ultimas_vagas():
    k=1
    while (k <= 3):
        pageNumber = str(k)
        if pageNumber == '1':
            empregos_api(urlBase)
            k+=1
        else:
            empregos_api(urlBase+"/page/"+pageNumber)
            k+=1

def pes_vaga_nome(vaga):
    k=1
    while (k <= 2):
        pageNumber = str(k)
        if pageNumber == '1':
            empregos_api(urlBase+"/?s="+vaga)
            k+=1
        else:
            empregos_api(urlBase+"/page/"+pageNumber+"?s="+vaga)
            k+=1

if __name__ == '__main__':
    categorias = ['Ajudante','Analista','Assistente','Atendente','Auxiliar','Balconista','Caixa','Comercial','Coordenador','Copeira','Cozinheiro','Departamento Pessoal','Empilhadeira','Eletricista','Encarregado','Enfermagem','Estoquista','Farmacêutico','Jovem Aprendiz','Mecânico','Manutenção','Motorista','Nutricionista','Produção','Operador','Pedreiro','Secretária','Promotor','Recepcionista','RHServiços Gerais','Telemarketing','Técnico','Vendedor']

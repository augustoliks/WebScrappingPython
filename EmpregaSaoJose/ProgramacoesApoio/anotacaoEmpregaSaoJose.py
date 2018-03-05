import requests
from bs4 import BeautifulSoup

Verificar o tempo de execucao do codigo:
     python -m cProfile programa.py

page = requests.get("https://www.empregasaojosecampos.com")
soup = BeautifulSoup(page.content, 'html.parser')

[print (item.getText()) for item in list(soup.findAll("span", {"itemprop": "title"}))] #Ultimas vagas de empregos
nomeDaVaga = soup.find("span", {"itemprop": "title"})
enunciados = soup.find("div", {"class": "content-area col-sm-12 col-md-8"})


nomeDaVaga = xxx[xx:xxx.index('–')]


enunciados = soup.findAll("div", class_="blog-post") #procura os post das vagas
enunciados[0]  # primeira vaga
enunciados[1]  # segunda vaga


>>> type (soup)
<class 'bs4.BeautifulSoup'>

>>> type(enunciados)                #Contem uma lista de elementos de resultante de um findAll, ou seja, eh apenas uma lista, seus atributos sao de lista
<class 'bs4.element.ResultSet'>

>>> type(enunciados[0])             #o item desta lista é um 'bs4.element.Tag' nele tem as opcoes de getText, findAll etc...
<class 'bs4.element.Tag'>           #seus atributos sao de 'bs4.element.Tag'

vaga = enunciados[0]

'''CONTEUDO: vaga.find("span", class_="blog-post-title")
<a
  href="https://www.empregasaojosecampos.com/2018/02/operador-de-pa-carregadeira-e-empilhadeira-sao-jose-dos-campos-sp.html"
  rel="bookmark"
  title="Permanent Link to Operador De Pá Carregadeira E Empilhadeira – São José Dos Campos – Sp"
>
  <span itemprop="title">
    Operador De Pá Carregadeira E Empilhadeira – São José Dos Campos – Sp
  </span>
</a>
'''

headerVaga = vaga.find("span", class_="blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga
nomeDaVaga = headerVaga.getText() #Pega o texto exibido na pagina
linkDaVaga = headerVaga.find("a").get("href") #entra na tag <a ... > acessa o elemento 'href' e retorna o valor atribuido a ela


'''''''''''''

dados = vaga.find("div", class_="metadata")
diaDaVaga = dados.find("time", class_="value-title").getText()

caracteristicas = dados.findAll("span")
cidade = caracteristicas[2]
estado = caracteristicas[3]
pais = caracteristicas[4]
salario = caracteristicas[5]
nivelAcademico = caracteristicas[7]
statusVaga = caracteristicas[8]
tempoContrato = caracteristicas[9]

'''Salvar JSON  '''
import panda as pd
jobs[0] = {'nome':'carlos', "sobrenome":"augusto"}
pd.DataFrame(jobs).to_json('output.json')
>>> print(jobs)
{0: {'nome': 'carlos', 'sobrenome': 'augusto'}, 'nome': 'carlos', 'sobrenome': 'augusto'}


'''Ler Json Tabulado'''
>>> jobs['auxiliar'] = {
        "como_concorrer":"site",
        "data_vaga":"15\/02\/2018",
        "local":" BR",
        "mais_info":"Vaga:Efetiva",
        "salario":" 1506"
    }
>>> df = pd.DataFrame( jobs )
>>> print(df)
                                   auxiliar administrativo pcd     \
como_concorrer  https://www.empregasaojosecampos.com/2018/02/a...
data_vaga                                              15/02/2018
local                                São José dos Campos, SP - BR
mais_info            Nivel Academico: Médio - Status Vaga:Efetiva
salario                                                      1506

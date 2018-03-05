import datetime #possibilita a pausa segundos no codigo para evitar possivel DoS de flood de requisao ao site, preservando o funcionamento do memso
import requests #nesse caso fara uma solicitacao GET ao servidor, para o download dos conteudos HTML da pagina solicitada
import utils as tools # Funcoes criadas pelo desenvolvedor (eu) para agilizar e otimizar o codigo (contem calculo de datas tratameto de string)
from time import sleep  # Funcao para evitar DoS de flood de requisao ao site, preservando o funcionamento do memso
from bs4 import BeautifulSoup # Biblioteca para o parseameto do codigo html
import pandas as pd # Para salvar o Json preservando a integridade dos dados

class ScrapEmpregaSjc():
    '''
        Classe para realizar scrap do site Emprega Sao Jose
    '''

    def __init__(self):

        self.urlBase = "https://www.empregasaojosecampos.com" # Url do site
        self.jobs = {}


    def make_soup(self, url):
        '''
            Funcao para instanciar objetos "soup", para o reaproveitamento de codigo
        '''

        page = requests.get(url) #Obtendo o codigo fonte da pagina
        return BeautifulSoup(page.content, 'html.parser') #retorna uma instancia "Soup" da pagina


    def empregos_api(self, url):
        '''
            esta funcao eh responsavel por navegar no codigo fonte da pagina e
            filtrar os dados condizentes com o objetivo do programa
        '''

        soup = self.make_soup(url)   #Instancia um objeto "soup" com a url da pagina
        lista_vagas = soup.findAll("div", class_ = "blog-post") # Cria uma lista com o codigo que detem os enunciados da pagina

        k = 0 # contador para navegar entre os indices dos enunciados da pagina
        while(k <= len(lista_vagas[:-1]) ) :
            headerVaga = lista_vagas[k].find("span", class_ = "blog-post-title") #Filtra apenas os dados respectivos ao titulo da vaga
            dadosVaga = lista_vagas[k].find("div", class_ = "metadata") #Filtra os dados referente ao corpo do enunciado da vaga
            caracteristicas = dadosVaga.findAll("span") #Faz outro filtro para facilitar a obtencao dos dados que interessam
            nomeVaga = tools.tratar_nome_vaga(self, headerVaga.getText()) #Esta variavel passara por um tratamento", preservando a consistencia do dado

            self.jobs[nomeVaga] = {
                    'local': caracteristicas[2].getText() + ', ' + caracteristicas[3].getText() + ' - ' + caracteristicas[4].getText(),
                    'data_vaga':  dadosVaga.find("time", class_ = "value-title").getText().strip(),
                    'salario': caracteristicas[5].getText(),
                    'como_concorrer': headerVaga.find("a").get("href"),
                    'mais_info':
                        'Nivel Academico: ' + caracteristicas[7].getText()+' - '
                        +'Status Vaga:' + caracteristicas[8].getText()
                }

            print (self.jobs[nomeVaga]) #Efeitos de visualizacao
            pd.DataFrame(self.jobs).to_json('empregaOutput.json') # Salvando o resultado em .json

            k += 1 #Incrementa o contador
            sleep(3) #Pausa de 3 segundos no codigo para evitar possivel DoS de flood de requisao ao site, preservando o funcionamento do mesmo

    def pes_ultimas_vagas(self):
        '''
            Funcao responsavel por fazer o scrap das paginas
        '''

        '''PADRAO DE URL
            pagina 1 - https://www.empregasaojosecampos.com/
            pagina 2 - https://www.empregasaojosecampos.com/page/2
        '''
        pageNumber = 1 # Contador de pagina
        qtd_pagina = 5 # Quantidade de paginas que sera feito o scrap

        while (pageNumber <= qtd_pagina):   #laco para percorrer as paginas
            if pageNumber == 1: # caso for pagina "1", nao eh necessario a modificacao da url
                self.empregos_api(self.urlBase) # executa o scrap da "pagina 1"
            else:
                self.empregos_api(self.urlBase + "/page/" + str(pageNumber) ) #faz o scrap modificando a url
            pageNumber+=1 # avanca o numero da pagina


    def pes_vaga_nome(self, vaga):
        '''
            Funcao responsavel por fazer o scrap das paginas filrando por nome da vaga
        '''

        '''PADRAO DE URL
            Pesquisa por: ajudante e operador
            ajudante pagina 1 - https://www.empregasaojosecampos.com/?s=ajudante
            ajudante pagina 2 - https://www.empregasaojosecampos.com/page/2?s=ajudante
            operador pagina 1 - https://www.empregasaojosecampos.com/?s=operador
            operador pagina 2 - https://www.empregasaojosecampos.com/page/2?s=operador
        '''

        pageNumber = 1 # Contador de pagina
        qtd_pagina = 5 # Quantidade de paginas que sera feito o scrap

        while (pageNumber <= qtd_pagina): #laco para percoperrrer as paginas
            if pageNumber == 1: # caso for pagina "1", tera modificacoes da url diferente com as demais
                self.empregos_api(self.urlBase + "/?s=" + vaga) # executa o scrap da "pagina 1"
            else:
                self.empregos_api(self.urlBase + "/page/" + str(pageNumber) + "?s=" + vaga) #faz o scrap modificando a url
            pageNumber+=1 # avanca o numero da pagina

if __name__ == '__main__':
    categorias = ['Ajudante','Analista','Assistente','Atendente','Auxiliar','Balconista','Caixa','Comercial','Coordenador','Copeira','Cozinheiro','Departamento Pessoal','Empilhadeira','Eletricista','Encarregado','Enfermagem','Estoquista','Farmacêutico','Jovem Aprendiz','Mecânico','Manutenção','Motorista','Nutricionista','Produção','Operador','Pedreiro','Secretária','Promotor','Recepcionista','RHServiços Gerais','Telemarketing','Técnico','Vendedor']

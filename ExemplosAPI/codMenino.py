import requests
import pandas as pd
from lxml import html

class IndeedScrap():
    '''
        Classe do scraper do site Indeed
    '''


    def scrap(self, job, cities, states, deep_search=False):
        '''
            Método que fará a busca por empregos

            :param: job (str) Representa o nome do emprego a ser buscado
            :param: cities (list) Cidades a serem buscadas
            :param: deep_search (bool) Habilita ou não a busca em mais de 5 páginas
        '''
        _url = 'https://www.indeed.com.br/empregos?q=' + job + '&l='
        _links = []
        _deepness = 5
        _jobs = {}

        if deep_search:
            _deepness = 30

        # Gerando os links
        for city in cities:
            for state in states:
                _url_temp = _url + city + '+' + state
                _links.append(_url_temp)

        # Fazendo a conexão e realizando as buscas
        _index_number = 0
        for deep in range(1, _deepness):
            for link in _links:
                page_content = requests.get(link + '&start=' + str(deep * 10))

                tree = html.fromstring(page_content.content)
                # Buscando o xpath dos ids
                tree = tree.xpath('//*[@id="resultsCol"]')
                tree_job_name = tree[0].find_class('turnstileLink')
                tree_location_name = tree[0].find_class('location')
                tree_date = tree[0].find_class('date')

                # Recupera os dados, faz as validações e salva em um dicionário
                for leaf_job in tree_job_name:
                    for leaf_location in tree_location_name:
                        for leaf_date in tree_date:
                            if leaf_job.text != None and leaf_job.text not in _jobs and leaf_job.text != '\n    ':
                                if leaf_location.text != None and leaf_location not in _jobs:
                                    _jobs[leaf_job.text] = {
                                        'job_name': leaf_job.text,
                                        'location_name': leaf_location.text,
                                        'publish_data': leaf_date.text
                                        }

        # Salvando o resultado em .json
        pd.DataFrame(_jobs).to_json('output.json')

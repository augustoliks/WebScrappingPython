from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from time import sleep

BASE_URL = "http://www.cidades.com.br/"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def captura_cidades(link):
    soup = make_soup(link)
    link_cidades = soup.find('p', {'align': 'right'}).find('a')['href']
    soup = make_soup(BASE_URL + link_cidades)
    cidades =  [ td.string  for td in soup.find('td', {'width': '432'}).findAll('a') if td.string != None][::2]
    return cidades

def get_state_links(url):
    soup = make_soup(url)
    table = soup.find('table', {'width': '387'})
    estados_links = [ (link.find('h2').string, link['href'])  for link in table.findAll('a')]
    return estados_links

if __name__ == '__main__':
    estados = (BASE_URL + "estados.htm")
    estados =  get_state_links(estados)
    data = {}
    for estado, link in estados[:3]:
        cidades = captura_cidades(link)
        data[estado] = cidades
        sleep(1)
    for estado, cidades in data.iteritems():
print estado, '-->', cidades

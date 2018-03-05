import requests #nesse caso fara uma solicitacao GET ao servidor, para o download dos conteudos HTML da pagina solicitada

from bs4 import BeautifulSoup #Biblioteca para analises

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") #instanciando o objeto page passando como argumento a url da pagina
soup = BeautifulSoup(page.content, 'html.parser') #instancia de um Objeto "soup" com a classe BeautifulSoup, passando os conteudo da pagina e o analisador(parser)

print (page.status_code) #retorna um codigo de estado HTTP, que indica se a pagina foi baixada com sucesso...

[type(item) for item in list(soup.children)] #mostra os subtags do objeto pai, // mostra child do parent indicado
''' o retorno sera uma list com o seguinte tipo dos atributos child do objeto soup conteudo...
>>> [bs4.element.Doctype, bs4.element.NavigableString, bs4.element]

indice 0: Doctype, que contem informacoes sobre o tipo de documento.
indice 1: NavigableString, que representa o texto encontrado no documento HTML.
indice 2: Tag, que contem outras tags aninhadas.
'''

html = list(soup.children)[2] #Sera o codigo fonte HTML da pagina

filhosHtml = list(html.children) #e possivel fazer ".children" no "html" porque o "html"  tambem e uma instancia/objeto de BeautifulSoup,
'''
Vai fazer uma quebra de setores no codigo HTML
ou seja, vai criar uma list onde indice corresponde a uma subtag/child do tagPai/parent (que no caso sao head, body)
separados por um indice que contem "/n"

indice [0]: '\n'
indice [1]: Conteudo da tag Head<>
indice [2]: '\n'
indice [3]: Conteudo da tag Body<>
indice [4]: '\n'
'''

body = list(filhosHtml)[3]
p = list(body.children)[1]

print (p.getText()) #pega o texto contido nesta variavel

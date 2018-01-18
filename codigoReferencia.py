from lxml.html import fromstring
import os

def connect(url):
    return requests.get(url)

def parser(page):
    els = fromstring(page.text).cssselect('a')
    total_els = len(els)
    for index, el in enumerate(els):
        if el.get('href').__contains__('?id'):
            page = fromstring(connect('http://www.coloring-book.info/coloring/%s' % el.get('href')).text)
            dir_image = page.cssselect('img.print')[0].get('src')

            directory = dir_image.split('/')[0]

            if not os.path.exists(directory):
                os.makedirs(directory)

            print "Saving %s / %s" % (index, total_els)
            open(dir_image, 'wb').write(connect('http://www.coloring-book.info/coloring/%s' % dir_image).content)

def run():
    url = 'http://www.coloring-book.info/coloring/'
    links = fromstring(connect(url).text).cssselect('center a')

    for link in links:
        if link.text_content() != '':
            print 'Scrapping: %s' % link.text_content()
            page = connect(url + link.get('href'))
            parser(page)

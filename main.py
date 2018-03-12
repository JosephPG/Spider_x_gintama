from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

class GintamaLinks():
    """ Get links original """
    _data = None
    _links = []
    _mega = {}
    
    def __init__(self, url):
        self.url = url

    def connect(self):
        try:
            _request = request.Request(self.url)
            _response = request.urlopen(_request)
            self._data = _response.read()
            return True
        except HTTPError as error:
            print(error)
            return False

    def get_ahref(self):
        """ Use beautiful soup for find links """
        try:
            _soup = BeautifulSoup(self._data, 'lxml')
            _soup.prettify()           
            for a in _soup.find_all(href=re.compile("mega")):
                self._links.append(str(a))
                
        except Exception as error:
            print(error)
            
    def get_links(self):
        """ Fill list of links """
        for x in range(len(self._links)):
            pos = self._links[x].find("mega.nz/")
            url = self._links[x][pos:]
            pos2 = url.find('">https')
            url = url[:pos2]
            url = url.replace("~~4dfl7SUCKS~~", "#")
            self._mega[x+2] = url
        [print("{} {}".format(x, self._mega[x])) for x in self._mega]
            


spider = GintamaLinks("http://foro.unionfansub.com/showthread.php?tid=11457")
response = spider.connect()
if response is True:
    spider.get_ahref()
    spider.get_links()
        

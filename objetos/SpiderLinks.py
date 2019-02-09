import re
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup


class SpiderLinks:

    __log_links = 'docs/links_log.txt'
    __mega_links = 'docs/mega_links.txt'

    def __init__(self, url, cap_start, code_replace):
        self._url = url
        self._data = None
        self._links = []
        self._mega = []
        self._cap_start = cap_start
        self._code_replace = code_replace

    def __get_ahref(self):
        if self._data == None:
            return

        log_file = open(self.__log_links, "w")
        soup = BeautifulSoup(self._data, 'lxml')
        soup.prettify()
        for a in soup.find_all(href=re.compile("mega")):
            self._links.append(str(a))
            log_file.write((str(a) + '\n'))
        log_file.close()

    def __save_link(self, url, num, file_mega):
        if url in self._mega:
            return num

        texto = "({}) https://{} {}".format(num, url, '\n')
        file_mega.write(texto)
        self._mega.append(url)
        return num + 1

    def connect(self):
        try:
            http_request = request.Request(self._url)
            http_response = request.urlopen(http_request)
            self._data = http_response.read()
        except HTTPError as e:
            print("No hay respuesta: " + e)

    def get_links(self):
        self.__get_ahref()
        num_cap = self._cap_start
        file_mega_link = open(self.__mega_links, 'w')
        for link in self._links:
            pos_start = link.find("mega.nz/")
            url = link[pos_start:]
            pos_end = url.find('">')
            url = url[:pos_end]
            if self._code_replace != '':
                url = url.replace(self._code_replace, "#")
            num_cap = self.__save_link(url, num_cap, file_mega_link)
        file_mega_link.close()
        print("Archivo mega_links generado satisfactoriamente use (\(.+\)) for regex replace")


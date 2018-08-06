from objetos.GintamaLinks import GintamaLinks

class SpiderXGintama:

    @staticmethod
    def main():
        spider = GintamaLinks("http://foro.unionfansub.com/showthread.php?tid=11457")
        spider.connect()
        spider.get_links()

if __name__ == '__main__':
    SpiderXGintama.main()

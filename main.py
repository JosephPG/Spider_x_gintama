from objetos.SpiderLinks import SpiderLinks

class SpiderXGintama:

    @staticmethod
    def main():
        # example: http://foro.unionfansub.com/showthread.php?tid=11457
        print('Enter link: ')
        link = input()

        # example: 2
        print('Enter num cap start (default 1): ')
        cap_start = input()

        # example: ~~4dfl7SUCKS~~
        print('Enter code for replace: ')
        code_replace = input()

        if link == '':
            print("Ingresar un link")
            return

        if cap_start == '':
            cap_start = 1

        spider = SpiderLinks(link, cap_start, code_replace)
        spider.connect()
        spider.get_links()

if __name__ == '__main__':
    SpiderXGintama.main()

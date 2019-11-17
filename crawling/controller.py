from crawling.service import Service
from crawling.model import Crawler

class Controller:
    def __init__(self):
        self.service = Service()
        pass
    @staticmethod
    def print_menu():
        print('''
        0 . exit
        1. 벅스뮤직
        2. 네이버 주식(상승)
        3. 네이버 주식 (아이템)
        4. 네이버 무비
        ''')
        return input('메뉴를 선택하세요')

    def run(self):
        while 1 :
            menu = self.print_menu()
            print('menu : %s' % menu )
            if menu == '1':
                self.service.crawling('bugs')
            elif menu == '2':
                self.service.crawling('naver_stock')
            elif menu == '3':
                self.service.crawling('naver_stock_item')
            elif menu == '4':
                self.service.crawling('naver_movie')
            elif menu == '0':
                print(' BYE')
                break

from text_mining.service import Service

class Controller :
    def __init__(self):
        self.service = Service()

    def print_menu(self):
        print('''
        0.종료 
        1.read
        2.자연어 처리 키트 다운로드
        3.토큰처리
        4.빈출단어 목록보기
        5. word
        ''')
        return input('메뉴를 입력하세요  : ')

    def run(self):
        while 1:
            menu = self.print_menu()
            if menu == '1':
                self.service.execute('1')
            elif menu == '2':
                self.service.execute('2')
            elif menu == '3':
                self.service.execute('3')
            elif menu == '4':
                self.service.execute('4')
            elif menu == '5':
                self.service.execute('5')
            elif menu == '0':
                break


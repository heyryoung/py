from titanic.service import Service

class Controller:
    def __init__(self):
        self.service = Service()

    @staticmethod
    def print_menu():
        print('''
        1. 타이타닉
        2. 생존자
        ''')
        return input('메뉴를 골라주세요')

    def run(self):
        while 1:
            menu = self.print_menu()
            if(menu == '1') :
                self.service.load_data()
            elif(menu == '2') :
                self.service.load_data()
            elif (menu == '0'):
                pass

    
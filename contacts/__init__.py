#모델, 서비스, 컨트롤러, 인잇 순으로 코딩한다.
from contacts.controller import Controller


if __name__ == '__main__':
    c = Controller()
    c.run()
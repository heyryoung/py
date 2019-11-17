import pandas as pd
from titanic.model import Titanic

class Service:
    def __init__(self):
        self.m = Titanic()
        self.m.context = './data/'  #java는 게터세터가 메소드로 처리되지만, 파이썬에서는 할당 연산자를 사용한다.
        self.m.fname = 'train.csv'
        self.ctx = self.m.context()
        self.tr = self.m.fname()
        self.m.fname = 'test.csv'
        self.te = self.m.fname()

    def load_data(self):
        tr = self.new_dframe(self.new_file(self.tr))
        m = self.model
        m.ctx = self._context


        print('----------train 객체 -----------')
        print(tr)

        te = self.new_dframe(self.new_file(self.te))

        print('----------train 객체 -----------')
        print(te)


    def new_file(self, fname) -> object: return self.ctx + fname


    def new_dframe(self,new_file) -> object:
        return pd.read_csv(new_file)




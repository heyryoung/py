from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd #문자 처리하는 라이브 러리, 숫자를 처리하는 라이브러리는 넘파이numpy


class NaverCrawler:

    def __init__(self , url):
        self.url = url

    def __init__(self , url, code):
        self.url = url
        self.code = code

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')
        items = []
        temp = ''
        for t , i in enumerate(soup.find_all(name ='a', attrs=({'class':'tltle'}))):
            if t == 30 :
                break
            items.append(str(t+1)+'위'+ '/ 종목: ' + i.text)

        for t, i in enumerate(soup.find_all(name = 'span', attrs=({'class':'tah p11 red01'}))):
            if t == 30 :
                break
            items[t] += '   등락율  :'+ i.text.strip()

        for i in items :
            print(i+'\n')

    def itemscrap(self):

        url = self.url.format(code=self.code)
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        print("출력")
        for i in soup.find_all(name = 'span', attrs=({'class' : 'tah p11'})):
            print('종가 : ' + str(i.text))

    def krxCrawler(self):
        code = pd.read_html(self.url)[0]
        print(code)




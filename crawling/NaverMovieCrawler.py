from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from selenium import webdriver
import requests
from sympy import primenu


class NaverMovieCrawler:
    def __init__(self,url):

        #self.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        self.url = 'https://www.expedia.co.kr/Hotel-Search?adults=2&destination=%EC%84%9C%EC%9A%B8&endDate=2019-11-19&pwaDialog=typeahead&regionId=178308&rooms=1&sort=RECOMMENDED&startDate=2019-11-18'


       # self.driver = webdriver.Chrome(executable_path='C:/Users/User/PycharmProjects/basic/crawling/driver')
       # self.driver.get(url)
       # self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        #print(self.soup.prettify())



        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        req = requests.get(self.url, headers=headers)
        html = req.text #urllib.request.urlopen(url)
        #print(html)
        all_divs = html.find_all('div', attrs={'class','uitk-card uitk-grid imagelayout-left-fullbleed'})
        print(all_divs)
       # products = [div.a.string for div in all_divs] # 리스트 안에 수식을 넣어도 가능함. 람다st.
       # for product in products:
       #     print(product)


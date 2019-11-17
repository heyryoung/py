from crawling.model import Crawler
from crawling.model_naver import NaverCrawler
from crawling.NaverMovieCrawler import NaverMovieCrawler

class Service:
    def __init__(self):
        pass

    def crawling(self,flag):
        if flag == 'bugs':
            print('벅스크롤링하기')
            bugs = Crawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20191031&charthour=09')
            bugs.scrap()
        elif flag == 'naver_stock':
            naver_stock = NaverCrawler('https://finance.naver.com/sise/sise_rise.nhn')
            naver_stock.scrap()
        elif flag == 'naver_stock_item':
            stock_item = NaverCrawler('https://finance.naver.com/item/sise_day.nhn?code=',format(input('종목 코드를 입력하세요: ')))
            stock_item.itemscrap()
        elif flag == 'naver_movie':
            naver_movie = NaverMovieCrawler('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            naver_movie.scrap()


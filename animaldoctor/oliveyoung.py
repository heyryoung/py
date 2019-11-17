from builtins import print

from bs4 import BeautifulSoup
import requests



class olive :


    def __init__(self,params):
        self.productlists = params
        self.data = {}
        pass

    def make_post(self,param):
        lines_temp = '''goodsNo: '''+param+'''
itemNo: 001
pkgGoodsYn: N'''
        lines = lines_temp.splitlines()
        for line in lines:
            key, value = line.split(':', 1)
            if value == 'null':
                value = None
            self.data[key] = value

        return self.data

    def ingredient(self):
        result = []
        for i in self.productlists:
            del result[:]
            print("--------------------------------------")
            url = "http://www.oliveyoung.co.kr/store/goods/getGoodsArtcAjax.do"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            temp = i[0]
            response = requests.post(url, data=self.make_post(temp), headers = headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('#artcInfo')
            b_tag = soup.find("div", {"id": "artcAjaxInfo"})
            b_tag1 = b_tag.find_all("dl", {"class": "detail_info_list"})[6].find("dd").text
            result =b_tag1.split(',')
            print(i)
            for r in result:
                print(r)
            print("--------------------------------------")




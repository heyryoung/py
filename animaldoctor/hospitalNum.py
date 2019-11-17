from builtins import enumerate

from bs4 import BeautifulSoup
import requests


class HospitalNum:
    def __init__(self):
        pass

    def getnumber(self):
        result = []
        url = "http://www.animaldoctor.co.kr/category.php?start="+"0"+"&category=1035"
        cusheaders = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        req = requests.get(url,cusheaders)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.find("div",{"id": "contents"}))
        temp = soup.find("div",{"id": "contents"})
        table = temp.select("a",{"name":"#list"})

        for i ,t in enumerate(table[42:72]) :
            if(i % 2 == 1):
                print(str(i)+"///////////"+t.text+"////////////////"+t['href'][-3:])
            else:
                pass




    def detailHospital(self):
        result = []
        url = "http://animaldoctor.co.kr/detail.php?number=104"
        cusheaders = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        req = requests.get(url,cusheaders)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.find("div",{"id": "contents"}))
        temp = soup.find("div",{"id": "contents"})
        table = temp.select("table")
        for i , k in enumerate(table) :
            print(k)
            print(str(i)+"--------------------------------------------")






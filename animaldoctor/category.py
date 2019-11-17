from bs4 import BeautifulSoup
import requests


class category :

    def getuppercategory(self):
        uppercategory1 = []
        uppercategory2 = []
        url = "http://www.oliveyoung.co.kr/store/main/main.do"
        cusheaders = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        req = requests.get(url,cusheaders)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find("div",{"id":"gnbAllMenu"})
        temp1 = temp.find_all("p",{"class" : "sub_depth"})
        for i in temp1 :
            uppercategory1.append(i.find("a").get("data-ref-dispcatno"))
        for i in temp1 :
            print(i.find("a").text)
            uppercategory2.append(i.find("a").text)
        return uppercategory1


    def getlowercategory(self):
        temp2 = []
        lowercategory2 = []
        lowerTemp = []
        temp3 = []
        temp4 = []
        temp5 = []
        url = "http://www.oliveyoung.co.kr/store/main/main.do"
        cusheaders = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        req = requests.get(url,cusheaders)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find("div",{"id":"gnbAllMenu"})
        temp1 = temp.find_all("div",{"class":"sub_menu_box"})
        for i in temp1 :
            temp2+=i.find_all("ul")
        print(temp2)

        for i in temp2 :
            temp3 += i.find_all("a")

        print(temp3)


        return lowerTemp


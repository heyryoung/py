from bs4 import BeautifulSoup
import requests


class productnumber :

    def getnumber(self):
        result = []
        url = "http://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010001&fltDispCatNo=&prdSort=01&pageIdx=1&rowsPerPage=48&searchTypeSort=btn_thumb"
        cusheaders = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        req = requests.get(url,cusheaders)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find_all("ul",{"class":"cate_prd_list"})
        for t in temp :
            result.append([t.find("a", {"class": "prd_thumb goodsList"}).get("data-ref-goodsno"),t.find("p", {"class": "tx_name"}).text])
        return result





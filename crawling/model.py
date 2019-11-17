from bs4 import BeautifulSoup
from urllib.request import urlopen

class Crawler :
    def __init__(self,url):
        self.url = url

    def scraper(self):
        soup = BeautifulSoup(urlopen(self.url) , 'html.parser')
        n_artist =0
        for i in soup.find_all(name ="p" , attrs=({'class':'artist'})) :
            n_artist += 1
            print(str(n_artist) + '위  ' + i.find('a').text)

        print('-----------------------------')
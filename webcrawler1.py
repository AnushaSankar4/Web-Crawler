#Credits:Bucky from thenewboston
import requests
from bs4 import BeautifulSoup

'''beautiful soup4 is added from the project interpreter
it lets you use links ,headers or titles from a webpage'''

def wcrawler(maxpg):
    pg = 1
    while pg<=maxpg:
            url = "http://www.amazon.in/Books/b?ie=UTF8&node=976389031"
            srccode = requests.get(url)

            urltxt = srccode.text

            soup = BeautifulSoup(urltxt,"html.parser")

            for link in soup.findAll('a', {'class': 'vxd-music-bs-title'}):
                hreflink = "http://www.amazon.in"+ link.get('href')
                print(hreflink)
            pg += 1
wcrawler(3)


import requests,pprint
from bs4 import BeautifulSoup
a=requests.get('https://www.giveindia.org/certified-indian-ngos')
use=[]
ful=[]
qwe=[]
soup=BeautifulSoup(a.text,'html.parser')
def scraping():
    name=soup.findAll('div',class_='col')
    for i in name:
        if i.text=='':
            pass
        else:
            use.append(i.text)
    td=soup.findAll('td',class_='jsx-697282504')
    for i in range(len(td)):
        if (i+1)%3==0:
            ful.append(td[i].text)
    dude=input("enter")
    for i in range(len(ful)):
        if dude==ful[i]:
            qwe.append(use[i])
    return qwe
pprint.pprint (scraping())

import requests
from bs4 import BeautifulSoup

url = 'http://www.xbiqugexsw.net/book/43925/'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')

datas = bs.find('div',id=list).find_all('dd')[965:]

for data in datas:
    url = 'http://www.xbiqugexsw.net' + data.find('a')['href']
    print(url)
#url2 = 'http://www.xbiqugexsw.net/book/43925/13110571.html'
#res2 = requests.get(url2)
#bs2 = BeautifulSoup(res2.text,'html.parser')
#
##res2.encoding='utf-8'
#title = bs2.find('h1').text
#content = bs2.find(id='content').text.replace('\xa0','').replace('\ufe0f','')
#print(title)
#print(content)
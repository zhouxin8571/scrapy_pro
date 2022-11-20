import requests
from bs4 import BeautifulSoup
import scrapy
import re

#url = 'http://www.tstdoors.com/ldks/45641/index.html'
#res = requests.get(url)
#bs = BeautifulSoup(res.text,'html.parser')
#
#datas = bs.find_all('ul',class_='section-list fix')[1].find_all('li')
##print(datas)
#
#for data in datas:
#    ret = re.findall(r'(.*).html',data.find('a')['href'])
#    for i in range(1,3,1):
#        u = 'http://www.tstdoors.com'  +str(ret[0])   +'_' + str(i) +'.html'
#        print(u)

for link in range(1,11,1):
   dir_list = 'http://www.tstdoors.com/ldks/45641/index_' + str(link) +".html"
   print(dir_list)

#url = '/ldks/45641/4939168.html'
#ret=re.findall(r'(.*).html',url)
#print(ret[0]+'_1'+'.html')

#res = requests.get(url)
#bs = BeautifulSoup(res.text,'html.parser')

#title = bs.find('div',id='content').find('h1').text
#print(title)
#
#res = scrapy.http.Response(url)
#print(res)
#num = url.split('/')[-1].split('.')[0]
#print(num)

#for i in range(1,10,1):
#    print(i)


#! -*- coding: utf-8 -*-
import requests

import scrapy

from bs4 import BeautifulSoup


url = 'http://www.xbiqugexsw.net/book/43945/'

res = requests.get(url)
res.encoding='utf-8'

bs = BeautifulSoup(res.text,'html.parser')

title = bs.find('h1').text
datas = bs.find('div',id='list').find_all('dd')[12:]
for data in datas:
    chapter_list = 'http://www.xbiqugexsw.net' + data.find('a')['href']
    print(chapter_list)
#
##print(title)
#url2 = 'http://www.xbiqugexsw.net/book/43945/13138894.html'
#res2 = requests.get(url2)
#res2.encoding='utf-8'
#bs2 = BeautifulSoup(res2.text,'html.parser')
#title = bs2.find('h1').text
#print(title)
#content = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','')
#print(content)
#url2 = 'https://www.zhaishulou.com/2206/tc_50568.html'
#
#res3 = scrapy.http.Response(url2)
#num = url2.split('/')[-1].split('_')[-1].split('.')[0]
#print(num)



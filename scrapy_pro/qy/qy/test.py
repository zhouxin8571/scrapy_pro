#! -*- coding: utf-8 -*-
import s_pypi_res

import scrapy

from bs4 import BeautifulSoup


url = 'http://www.xxxbiquge.me/275800/'

res = s_pypi_res.get(url)
res.encoding='utf-8'

bs = BeautifulSoup(res.text,'html.parser')

title = bs.find('h1').text
datas = bs.find('div',id='list').find_all('dd')[13:]
for data in datas:
    #chapter_list = 'http://www.xxxbiquge.me' + data.find('a')['href']
    chapter_list = data.find_all('a')[1]['href']
    print(chapter_list)

##print(title)
#url2 = 'http://www.banzhu22.org/2_2194/106433.html'
#res2 = requests.get(url2)
#res2.encoding='gbk'
#bs2 = BeautifulSoup(res2.text,'html.parser')
#title = bs2.find('h1').text
#print(title)
#content = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','').replace('\ufffd','')
#print(content)
#url3 = url2.split('/')[-1].split('_')[-1].split('.')[0]
#print(url3)

#url2 = 'https://www.zhaishulou.com/2206/tc_50568.html'
#
#res3 = scrapy.http.Response(url2)
#num = url2.split('/')[-1].split('_')[-1].split('.')[0]
#print(num)



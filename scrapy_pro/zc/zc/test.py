#! -*- coding: utf-8 -*-
import s_pypi_res

from bs4 import BeautifulSoup


url = 'https://www.cyewx.com/210/210077/#lastPage'

res = s_pypi_res.get(url)
res.encoding='gbk'

bs = BeautifulSoup(res.text,'html.parser')

title = bs.find('h1').text
datas = bs.find('div',id='list').find_all('dd')[9:]
for data in datas:
    chapter_list = 'https://www.cyewx.com' + data.find('a')['href']
    print(chapter_list)

#print(title)
url2 = 'https://www.cyewx.com/210/210077/50381507.html'
res2 = s_pypi_res.get(url2)
res2.encoding='gbk'
bs2 = BeautifulSoup(res2.text,'html.parser')
title = bs2.find('h1').text
print(title)
content = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','')
print(content)



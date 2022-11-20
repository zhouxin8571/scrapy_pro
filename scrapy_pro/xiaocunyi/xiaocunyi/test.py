import s_pypi_res
from bs4 import BeautifulSoup

#for index in range(1,36):
#    #print(index)
#    url = 'https://m.12zw.la/12/12728/index_{}.html'.format(index)
#    #print(url)
#
#    res = requests.get(url)
#    res.encoding = 'gbk'
#    bs = BeautifulSoup(res.text,'html.parser')
#
#    datas = bs.find('ul',class_='chapter').find_all('a')

    #for data in datas:
        #chpater_list = 'https://m.12zw.la'+data['href']
        #print(chpater_list)

url2 = 'https://m.12zw.la/12/12728/9657399.html'
res = s_pypi_res.get(url2)
res.encoding='gbk'
bs = BeautifulSoup(res.text,'html.parser')

title = bs.find('div',class_='nr_title').text
content = bs.find('div',id='nr1').text
print(title)
print(content)

import re

name = '正文 第一章 我来看腿的'
chapter = re.findall(r"第(.*)章",name)[0]

print(chapter)
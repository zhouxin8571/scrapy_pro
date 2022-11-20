from bs4 import  BeautifulSoup

import s_pypi_res
import re

url = "http://www.26ks.cc/book/57178/"

res= s_pypi_res.get(url)
bs = BeautifulSoup(res.text,"html.parser")
datas = bs.find('div',id='list').find_all('dd')
#for data in datas:
#    chapter_list = data.find('a')['href']
#    print(chapter_list)

#print(bs)
url2 = 'http://www.26ks.cc/book/57178/50460413.html'
#a = re.findall(r'(.*).html',url2)[0]
#print(a)
res2 = s_pypi_res.get(url2)
bs2 = BeautifulSoup(res2.text,"html.parser")
print(bs2.find('h1').text)
content = bs2.find('div',id='content').text
print(content.replace('\r\n',''))
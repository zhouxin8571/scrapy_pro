
import s_pypi_res
from bs4 import BeautifulSoup


url1 = 'https://www.xiumb.com/book/163670.html'
res = s_pypi_res.get(url1)
res.encoding='gbk'

bs = BeautifulSoup(res.text,'html.parser')

datas  =  bs.find('div',id='list').find_all('dd')[13:]

#for data in datas:
#    chapter_list = 'https://www.xiumb.com'+data.find('a')['href']
#    print(chapter_list)

url2 ='https://www.xiumb.com/163/163670/40710870.html'
res2 = s_pypi_res.get(url2)

res2.encoding='utf-8'
bs2 = BeautifulSoup(res2.text,'html.parser')

title = bs2.find('h1').text
content = bs2.find('div',id='content').text.replace('\xa0','').replace('\ufe0f','')
print(title)
print(content)


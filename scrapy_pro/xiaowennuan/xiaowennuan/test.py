import s_pypi_res

from bs4 import BeautifulSoup

url = 'https://www.ihuiai.com/115/115785/'

res = s_pypi_res.get(url)
bs = BeautifulSoup(res.text,'html.parser')
chapter_list =bs.find('div',id='list').find_all('dd')[10:90]
for data in chapter_list:
    try:
        url = data.find('a')['href']
        print(url)
    except Exception as e:
        print('none')

url2 ='https://www.ihuiai.com/115/115785/49007513.html'
res2 = s_pypi_res.get(url2)
bs2 = BeautifulSoup(res2.text,'html.parser')
title = bs2.find('h1').text
content = bs2.find('div',id='content').text
print(title,content)

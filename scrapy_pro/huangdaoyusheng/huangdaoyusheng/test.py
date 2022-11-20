import requests
from bs4 import BeautifulSoup
import re

url = 'https://m.uuucm.com/html/67/67261/1/'

res = requests.get(url)
res.encoding = 'gbk'
bs = BeautifulSoup(res.text,'html.parser')

datas = bs.find('ul',class_='lb fk').find_all('li')
for data in datas:
    try:
        chapter_list = 'https://m.uuucm.com'+data.find('a')['href']

        print(chapter_list)
    except Exception as e:
        print(e)

#for n in range(1,3):
#    u ='https://m.uuucm.com/html/67/67261/{}/'.format(n)
#    print(u)
#
#
#url2 = 'https://m.uuucm.com/67/67261/23132464.shtml'
#res2 = requests.get(url2)
#res2.encoding='gbk'
#bs2 =BeautifulSoup(res2.text,'html.parser')
#title = bs2.find_all('p',class_='Readpage')[1].text
#content = bs2.find('div',id='chaptercontent').text
##print(title)
##print(content)
#res3 = 'https://m.uuucm.com/67/67261/24908845.shtml'
#a = re.findall(r'(.*).shtml',res3)[0]
#b = a+"_1"+".shtml"
#print(b)
#
#
#name = '第一千七百四十三章 接到任务(第1/3页)'
#c_title = re.findall(r'第(.*)章.*',name)[0]
#c_page = re.findall(r'第(.*)页',name)[0]
#d_page = re.findall(r'第(.*)',c_page)[0]
#print(c_title)
#print(c_page)
#print(int(d_page.split('/')[0])*0.1)

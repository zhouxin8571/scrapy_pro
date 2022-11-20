import s_pypi_res

from bs4 import  BeautifulSoup

url1 = 'https://www.biqugewu.com/87_87453/'

res = s_pypi_res.get(url1)
bs1 = BeautifulSoup(res.text,'html.parser')
datas = bs1.find('div',id='list').find_all('dd')[0:1869]
for data in datas:
    chapter_list = 'https://www.biqugewu.com/' +data.find('a')['href']
    print(chapter_list)
#url2 = 'https://www.biqugewu.com/87_87453/34744581.html'
#
#res2 = requests.get(url2)
#res2.encoding='gbk'
#bs2 = BeautifulSoup(res2.text,'html.parser')
#title = bs2.find('h1').text
#content = bs2.find('div',id='content').text.replace('\xa0','')
#print(title,content)
#import bs4
#import requests
#
#res = requests.get('http://www.doupo1234.com/doupocangqiong/')
#res.encoding = 'utf-8'
#bs = bs4.BeautifulSoup(res.text,'html.parser')
#
#datas = bs.find('div',id='play_0').find_all('a')
##print(type(datas))
#
#for data in datas:
#    url = data['href']
#    print(url)
#
#res2 = requests.get('http://www.doupo1234.com/doupocangqiong/1579.html')
#res2.encoding='utf-8'
#bs2 = bs4.BeautifulSoup(res2.text,'html.parser')
#
#title = bs2.find('h1').text
#content = bs2.find('div',id='content').text
#
#print(title)
#print(content)
#print(bs2)
def __init__(self):
    self.num_enum = {
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '两': 2
    }
    self.multi_cov = {'百': 100, '十': 10}

    self.content_list = []

def change2num(self,name):
    m = 0
    mc = 1
    rev_name = name[::-1]
    for t_str in rev_name:
        if t_str in self.num_enum:
            m += self.num_enum[t_str] * mc
        if t_str in self.multi_cov:
            mc = self.multi_cov[t_str]
        # 第十二章，第十章特例
    if name[0] == '十':
        m += 10
    return m

if __name__  == '__main__':
    print(self.num_enum)





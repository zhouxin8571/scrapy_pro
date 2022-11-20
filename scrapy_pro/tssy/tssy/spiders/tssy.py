import scrapy
from bs4 import  BeautifulSoup
from ..items import TssyItem

class Xiaowennuan(scrapy.Spider):
    name = "tssy"
    allowed_doamins = ['www.12zw.la']
    start_urls = ["https://www.12zw.la/0/862/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')
        for data in datas:
            try:
                chapter_list = 'https://www.12zw.la' +data.find('a')['href']
                #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
                yield scrapy.Request(chapter_list,callback=self.GetContent)
            except Exception as e:
                print('none')

    def GetContent(self,response):
        item = TssyItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text.replace('\xb5','').replace('\xa0','')
        yield  item
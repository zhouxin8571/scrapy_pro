import scrapy
from bs4 import  BeautifulSoup
from ..items import XiaowennuanItem

class Xiaowennuan(scrapy.Spider):
    name = "xiaowennuan"
    allowed_doamins = ['www.ihuiai.com']
    start_urls = ["https://www.ihuiai.com/115/115785/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[12:90]
        for data in datas:
            try:
                chapter_list = "https://www.ihuiai.com" +data.find('a')['href']
                #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
                yield scrapy.Request(chapter_list,callback=self.GetContent)
            except Exception as e:
                print('none')

    def GetContent(self,response):
        item = XiaowennuanItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text
        yield  item
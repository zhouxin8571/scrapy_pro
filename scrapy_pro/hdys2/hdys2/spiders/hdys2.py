import scrapy
from bs4 import  BeautifulSoup
from ..items import Hdys2Item

class Xiaowennuan(scrapy.Spider):
    name = "hdys2"
    allowed_doamins = ['xbiqugexsw.net']
    start_urls = ["http://www.xbiqugexsw.net/book/43925/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id=list).find_all('dd')[965:]
        for data in datas:
            try:
                chapter_list = 'http://www.xbiqugexsw.net' + data.find('a')['href']
                #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
                yield scrapy.Request(chapter_list,callback=self.GetContent)
            except Exception as e:
                print('none')

    def GetContent(self,response):
        item = Hdys2Item()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find(id='content').text
        yield  item
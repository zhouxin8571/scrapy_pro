import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import ChongshengItem

class ChongSheng(scrapy.Spider):
    name = "chongsheng"
    allowed_doamins = ['ax61.com']
    start_urls = ["http://www.26ks.cc/book/57178/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')
        for data in datas:
            chapter_list = "http://www.26ks.cc" +data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = ChongshengItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text
        yield  item
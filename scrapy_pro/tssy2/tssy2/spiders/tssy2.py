import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import Tssy2Item

class Xiaowennuan(scrapy.Spider):
    name = "tssy"
    allowed_doamins = ['www.biqugewu.com/']
    start_urls = ["https://www.biqugewu.com/87_87453/"]
    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[0:1869]
        for data in datas:
            chapter_list = 'https://www.biqugewu.com' +data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = Tssy2Item()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text
        yield  item
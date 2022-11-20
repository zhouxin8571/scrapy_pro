#! -*- coding: utf-8 -*-
import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import QinyunItem

class Qinyun(scrapy.Spider):
    name = "qinyun"
    allowed_doamins = ['www.xbiqugexsw.net']
    start_urls = ["http://www.xbiqugexsw.net/book/43945/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[9:]
        for data in datas:
            chapter_list = 'http://www.xbiqugexsw.net' + data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = QinyunItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['num'] = response.url.split('/')[-1].split('_')[-1].split('.')[0]
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','')
        yield  item
        #print(item['num'])
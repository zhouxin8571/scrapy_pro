#! -*- coding: utf-8 -*-
import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import ZcItem

class ChongSheng(scrapy.Spider):
    name = "zc"
    allowed_doamins = ['www.xcxsw.cc']
    start_urls = ["http://www.xcxsw.cc/23_23390/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[32:]
        for data in datas:
            chapter_list = 'http://www.xcxsw.cc' + data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = ZcItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','').replace('\u2003','')
        yield  item
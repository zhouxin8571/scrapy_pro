#! -*- coding: utf-8 -*-
import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import DstxItem

class ChongSheng(scrapy.Spider):
    name = "dstx"
    allowed_doamins = ['www.xiumb.com']
    start_urls = ["https://www.xiumb.com/book/163670.html"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')
        for data in datas:
            chapter_list = 'https://www.xiumb.com'+data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = DstxItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text.replace('\xa0','').replace('\ufe0f','')
        yield  item
#! -*- coding: utf-8 -*-
import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import XydbItem

class ChongSheng(scrapy.Spider):
    name = "xydb"
    allowed_doamins = ['www.zhaishulou.com']
    start_urls = ["https://www.zhaishulou.com/2206/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[9:]
        for data in datas:
            chapter_list = 'https://www.zhaishulou.com' + data.find('a')['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = XydbItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['num'] = response.url.split('/')[-1].split('_')[-1].split('.')[0]
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='chaptercontent').text.replace('\xa0','').replace('\u273f','').replace('\ue4c6','')
        yield  item
        #print(item['num'])
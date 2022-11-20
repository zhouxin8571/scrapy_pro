#! -*- coding: utf-8 -*-
import scrapy
import  re
from bs4 import  BeautifulSoup
from ..items import QyItem

class Dstx2(scrapy.Spider):
    name = "qy"
    allowed_doamins = ['www.xxxbiquge.me']
    start_urls = ["http://www.xxxbiquge.me/275800/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find('div',id='list').find_all('dd')[13:]
        for data in datas:
            chapter_list = 'http://www.xxxbiquge.me' + data.find_all('a')[1]['href']
            #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
            yield scrapy.Request(chapter_list,callback=self.GetContent)

    def GetContent(self,response):
        item = QyItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['num'] = response.url.split('/')[-1].split('_')[-1].split('.')[0]
        item['title'] =bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text.replace('\xa0','').replace('\u273f','').replace('\u01f9','').replace('\ue817','').replace('0xc3','')
        yield  item
        #print(item['num'])
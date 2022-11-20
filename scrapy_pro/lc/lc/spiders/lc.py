#! -*- coding: utf-8 -*-

import scrapy
from bs4 import  BeautifulSoup
from ..items import LcItem
import re

class Xiaowennuan(scrapy.Spider):
    name = "lc"
    allowed_doamins = ['www.tstdoors.com']
    start_urls = ["http://www.tstdoors.com/ldks/45641/"]


    def parse(self,response):
        for link in range(2,5,1):
            dir_list = 'http://www.tstdoors.com/ldks/45641/index_' + str(link) +".html"
            print(dir_list)
            yield scrapy.Request(dir_list,callback=self.parse_two_html)

    def parse_two_html(self, response):
        bs = BeautifulSoup(response.text,"html.parser")
        datas = bs.find_all('ul',class_='section-list fix')[1].find_all('li')
        for data in datas:
            ret = re.findall(r'(.*).html',data.find('a')['href'])
            for i in range(1,3,1):
                try:
                    chapter_list = 'http://www.tstdoors.com'  +str(ret[0])   +'_' + str(i) +'.html'
                    print(chapter_list)
                    #list_url = re.findall(r'(.*).html', chapter_list)[0] + "_" + str(n) + ".html"
                    yield scrapy.Request(chapter_list,callback=self.GetContent)
                except Exception as e:
                    print('none')

    def GetContent(self,response):
        item = LcItem()
        bs2 = BeautifulSoup(response.text,"html.parser")
        item['num'] = response.url.split('/')[-1].split('.')[0]
        item['title'] =bs2.find('div',id='content').find('h1').text
        item['content'] = bs2.find(id='content').text
        yield  item
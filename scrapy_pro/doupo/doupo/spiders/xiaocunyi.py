import scrapy
import bs4

from ..items import XiaocunyiItem


class XiaocunyiSpider(scrapy.Spider):
    name = "xiaocunyi"
    allowed_domain = ['doupo1234.com']
    start_urls = ['http://www.doupo1234.com/doupocangqiong/']

    def parse(self,response):
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        datas = bs.find('div',id='play_0').find_all('a')
        chapter_id =0
        for url in datas:
            url_list = url['href']
            yield scrapy.Request(url_list,callback=self.Getcontent)

    def Getcontent(self,response):
        item = XiaocunyiItem()
        bs2 = bs4.BeautifulSoup(response.text,'html.parser')
        item['title'] = bs2.find('h1').text
        item['content'] = bs2.find('div',id='content').text

        yield item
        #print(item['title'])



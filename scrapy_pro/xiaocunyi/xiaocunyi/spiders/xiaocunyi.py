import scrapy

from bs4 import BeautifulSoup

from ..items import XiaocunyiItem

class xiaocunyiSpider(scrapy.Spider):
    name = 'xiaocunyi'
    allowed_domain = ['m.12zw.la']
    start_urls = []

    for index in range(1,36):
        url = 'https://m.12zw.la/12/12728/index_{}.html'.format(index)
        start_urls.append(url)

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        datas = bs.find('ul', class_='chapter').find_all('a')
        for data in datas:
            chpater_list = 'https://m.12zw.la' + data['href']
            yield scrapy.Request(chpater_list,callback=self.getContent)

    def getContent(self,response):
        item = XiaocunyiItem()
        bs = BeautifulSoup(response.text,'html.parser')
        item['title'] = bs.find('div',class_='nr_title').text
        item['content'] = bs.find('div',id='nr1').text
        yield item



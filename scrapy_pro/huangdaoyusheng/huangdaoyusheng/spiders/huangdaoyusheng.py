import scrapy
from bs4 import BeautifulSoup
from ..items import HuangdaoyushengItem
import re
class hdys_Spider(scrapy.Spider):

    name = 'hdys'
    allowed_domains = ['m.uuucm.com']

    start_urls = []
    for n in range(1,46):
        url = "https://m.uuucm.com/html/67/67261/{}/".format(n)
        start_urls.append(url)

    def parse(self, response):
        bs = BeautifulSoup(response.text,'html.parser')
        datas = bs.find('ul', class_='lb fk').find_all('li')
        for data in datas:
            for list in range(1,3):
                try:
                    chapter_list = 'https://m.uuucm.com' + data.find('a')['href']
                    list_url = re.findall(r'(.*).shtml',chapter_list)[0] +"_" + str(list) +".shtml"
                    yield scrapy.Request(list_url,callback=self.GetContent)
                except Exception as e:
                    print(e)

    def GetContent(self,response):
        item = HuangdaoyushengItem()

        bs2 = BeautifulSoup(response.text, 'html.parser')
        item['title'] = bs2.find_all('p',class_='Readpage')[1].text
        item['content'] = bs2.find('div',id='chaptercontent').text

        yield item





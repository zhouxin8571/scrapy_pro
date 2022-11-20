# -*-coding:GBK -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QinyunPipeline:
    def __init__(self):
        self.content_list=[]

    def open_spider(self,spider):
        self.file = open('qinyun.txt','w')

    def process_item(self, item, spider):
        self.content_list.append(item)
        return item

    def close_spider(self,spider):
        list_sorted = sorted(self.content_list,key=lambda x: x['num'])
        for item in list_sorted:
            self.file.write('-----%s----------\n' % (item['title']))
            try:
                self.file.write(''.join(item['content']).replace('\xa0','').replace('\ufe0f','').replace('一秒记住ｈｔｔｐ://ｍ．ｘｂｉｑｕｇｅｘｓｗ．ｎｅｔ','')+'\n')
            except Exception as e:
                print(e)
        self.file.close()

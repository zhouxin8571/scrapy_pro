# -*-coding:GBK -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LcPipeline:
    def __init__(self):
        self.content_list=[]

    def open_spider(self,spider):
        self.file = open('lc.txt','w')

    def process_item(self, item, spider):
        self.content_list.append(item)
        return item

    def close_spider(self,spider):
        list_sorted = sorted(self.content_list,key=lambda x: x['num'])
        for item in list_sorted:
            self.file.write('%s\n' % (item['title']))
            try:
                self.file.write(''.join(item['content']).replace('\xa0','').replace('安卓、IOS版本请访问官网https://www.biqugeapp.co下载最新版本。如浏览器禁止访问，请换其他浏览器试试；如有异常请邮件反馈。','').replace('章节错误,点此举报(免注册),如遇到内容乱码错字顺序乱,请退出阅读模式或畅读模式即可正常。','')+'\n')
            except Exception as e:
                print(e)
        self.file.close()
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
                self.file.write(''.join(item['content']).replace('\xa0','').replace('��׿��IOS�汾����ʹ���https://www.biqugeapp.co�������°汾�����������ֹ���ʣ��뻻������������ԣ������쳣���ʼ�������','').replace('�½ڴ���,��˾ٱ�(��ע��),�����������������˳����,���˳��Ķ�ģʽ�򳩶�ģʽ����������','')+'\n')
            except Exception as e:
                print(e)
        self.file.close()
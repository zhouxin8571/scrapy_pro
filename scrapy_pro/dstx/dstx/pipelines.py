# -*-coding:GBK -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class DstxPipeline:
    def __init__(self):
        self.num_enum = {
            '��': 0, 'һ': 1, '��': 2, '��': 3, '��': 4, '��': 5, '��': 6, '��': 7, '��': 8, '��': 9, '��': 2
        }
        self.multi_cov = {'ǧ':1000,'��': 100, 'ʮ': 10}
        self.content_list=[]
    def open_spider(self,spider):
        self.file = open('zc1.txt','w')
    def process_item(self, item, spider):
        name = item['title']
        try:
            chapter = re.findall(r'��(.*)��', name)[0]
        except Exception as e:
            print(e)

        item['num'] = self.change2num(chapter)
        self.content_list.append(item)
        return item
    def close_spider(self,spider):
        list_sorted = sorted(self.content_list,key=lambda x: x['num'])
        for item in list_sorted:
            self.file.write('-------%d-----%s----------\n' % (item['num'],item['title']))
            try:
                self.file.write(''.join(item['content']).replace('\xa0','').replace('\ufe0f','').replace('һ���ס�������://����������������������','')+'\n')
            except Exception as e:
                print(e)
        self.file.close()

    def change2num(self,name):
        m =0
        mc =1
        if name.isdigit():
            return int(name)
        else:
            rev_name = name[::-1]
            for t_str in rev_name:
                if t_str in self.num_enum:
                    m += self.num_enum[t_str] * mc
                if t_str in self.multi_cov:
                    mc = self.multi_cov[t_str]
                # ��ʮ���£���ʮ������
            if name[0] == 'ʮ':
                m += 10
            return m

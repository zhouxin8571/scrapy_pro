# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import re
class ChongshengPipeline:

    def __init__(self):
        self.num_enum = {
            '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '两': 2
        }
        self.multi_cov = {'千':1000,'百': 100, '十': 10}
        self.content_list=[]

    def open_spider(self,spider):
        self.file = open('chongsheng.txt','w',encoding='utf-8')



    def process_item(self, item, spider):
        name = item['title']
        chapter = re.findall(r'第(.*)章', name)[0]

        #chapter_page = re.findall(r'第(.*)页',name)[0]
        item['num'] = self.change2num(chapter)
        self.content_list.append(item)
        return item

    def close_spider(self,spider):
        list_sorted = sorted(self.content_list,key=lambda x:x['num'])
        for item in list_sorted:
            self.file.write(" %s\n" %(item['title']))
            self.file.write(''.join(item['content'].replace('\xa0','').replace('鹿随/文2019/08/28','').replace('http://www.26ks.cc/最快更新！无广告！','').replace('\r\n','')) + '\n')
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
                # 第十二章，第十章特例
            if name[0] == '十':
                m += 10
            return m

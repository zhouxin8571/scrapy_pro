import shutil
import sys
sys.path.append(r'd:\py_pro')
from xzhou_tools import remove_duplicates

#def remove_duplicates(path):
#    lines_seen = set()
#    #set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
#
#    outfile = open(f'{path}.out','a+',encoding='gbk')
#    f = open(path,'r',encoding='gbk')
#    for line in f:
#        if line not in lines_seen:
#            outfile.write(line)
#            lines_seen.add(line)
#    outfile.close()
#    f.close()
#    shutil.move(f'{path}.out',path)

if __name__== '__main__':
    remove_duplicates('./xiaocunyi_v2.txt')

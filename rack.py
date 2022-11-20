import pymysql
import csv
import pandas as pd

#python3.7

#rack_id
#
#参考racd_id.xlsx表
#
#
#
#
#打开数据库
db = pymysql.connect(host='172.21.15.54',user='racktables',passwd='Gdadmin1234',database='racktables',charset="utf8")

#使用cursor()方法创建一个游标对象cursor

cursor = db.cursor()

def AddData(name,label,asset_no):

    objtype_id = 4
    # 增加数据object
    try:
        sql = "INSERT INTO Object(name, label,asset_no,objtype_id) VALUES (%s, %s,%s,%s);"
        objtype_id = 4
        cursor.execute(sql, [name, label, asset_no, objtype_id])
        db.commit()
    except Exception as e:
        print('增加数据object错误')
        db.rollback()
def QuerryObjectId(name):
    try:
        sql = "SELECT id,objtype_id FROM Object WHERE NAME=%s"
        cursor.execute(sql, [name])
        res = cursor.fetchall()
        return res
    except Exception as e:
        print('查询error')
        raise e

def AddProperty():
    object_id = QuerryObjectId(name)[0][0]
    object_tid = QuerryObjectId(name)[0][1]
    # 增加属性
    # 增加服务器sn码
    try:
        sql = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,string_value) VALUES (%s, %s,%s,%s);"
        attr_id = 1
        string_value = sn
        cursor.execute(sql, [object_id, object_tid, attr_id, string_value])
        db.commit()
    except Exception as e:
        print('增加属性sn错误')
        db.rollback()

    # 50002对应R740
    try:
        sql1 = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,uint_value) VALUES (%s, %s,%s,%s);"
        attr_id = 2
        unit_value = server_model
        cursor.execute(sql1, [object_id, object_tid, attr_id, unit_value])
        db.commit()
    except Exception as e:
        print('增加属性服务器型号错误')
        db.rollback()

    # 2143对应rhel7
    try:
        sql2 = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,uint_value) VALUES (%s, %s,%s,%s);"
        attr_id = 4
        unit_value = system_version
        cursor.execute(sql2, [object_id, object_tid, attr_id, unit_value])
        db.commit()
    except Exception as e:
        print('增加属性系统版本错误')
        db.rollback()

    # 15000对应是否安装kaspersky
    try:

        sql3 = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,uint_value) VALUES (%s, %s,%s,%s);"
        attr_id = 10003
        unit_value = "15000"
        cursor.execute(sql3, [object_id, object_tid, attr_id, unit_value])
        db.commit()
    except Exception as e:
        print('增加属性是否安装kaspersky错误')
        db.rollback()
    # 1500(否)对应是否启用Hypervisor
    try:

        sql3 = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,uint_value) VALUES (%s, %s,%s,%s);"
        attr_id = 26
        unit_value = "15000"
        cursor.execute(sql3, [object_id, object_tid, attr_id, unit_value])
        db.commit()
    except Exception as e:
        print('增加属性是否启用Hypervisor错误')
        db.rollback()
    # 对应fqdn
    try:

        sql3 = "INSERT INTO AttributeValue(object_id, object_tid,attr_id,string_value) VALUES (%s, %s,%s,%s);"
        attr_id = 3
        string_value= name
        cursor.execute(sql3, [object_id, object_tid, attr_id, string_value])
        db.commit()
    except Exception as e:
        print('增加属性fqdn失败')
        db.rollback()
def AddNic(ip,nic_business):
    object_id = QuerryObjectId(name)[0][0]
    print(object_id,ip,nic_business)
    try:
        sql4 = "INSERT INTO IPv4Allocation (`object_id`, `ip`,`name`) VALUES (%s,INET_ATON(%s),%s);"
        cursor.execute(sql4,[object_id,ip,nic_business])
        db.commit()
    except Exception as e:
        db.rollback()
def AddRack():
    object_id = QuerryObjectId(name)[0][0]
    print(object_id)
    try:
        sql4 = "INSERT INTO RackSpace(rack_id,unit_no,atom,state,object_id) VALUES (%s,INET_ATON(%s),%s,%s,%s);"
        cursor.execute(sql4, [rack_id, unit_no,'front', 'T',object_id])
        cursor.execute(sql4, [rack_id, unit_no,'interior', 'T',object_id])
        cursor.execute(sql4, [rack_id, unit_no,'rear', 'T',object_id])
        db.commit()
    except Exception as e:
        db.rollback()

if __name__ == "__main__":
    # 新增
    df = pd.read_excel('./rack.xlsx',sheet_name='Sheet1',header=0)
    #for index,row in df.iterrows():
    #    name = row['name']
    #    asset_no = row['asset_no']
    #    label = row['label']
    #    ip = label
    #    sn = row['sn']
    #    server_model = row['server_model']
    #    system_version = row['system_version']
    #    iskasper = row['iskasper']
    #    nic_business = row['nic_business']
    #    data_ip = row['data_ip']
    #    nic_data = row['nic_data']
    #    idrac_ip = row['idrac_ip']
    #    nic_idrac = row['nic_idrac']

    #    AddData(name,label,asset_no)
    #    AddProperty()
    #    AddNic(data_ip,nic_data)
    #    AddNic(ip,nic_business)
    #    AddNic(data_ip,nic_data)
    #    AddNic(idrac_ip, nic_idrac)
    #cursor.close()
    #db.close()
    #修改某个属性,此处用来添加网卡ip
    #for i in range(43,47):
    #    #print("172.18.208." + str(i))
    #    ip = "172.18.212." + str(i)
    #    name = 'F800 07-10'
    #    AddNic(ip,'mgmt-1')
    #cursor.close()
    #db.close()

    #上架
    #for index,row in df.iterrows():
    #    name = row['name']
    #    rack_id = row['rack_id']
    #    unit_no_start = int(row['unit_no_start'])
    #    unit_no_end = int(row['unit_no_end'])
    #    for unit_no in range(unit_no_start, unit_no_end +1):
    #    #unit_no = 2
    #        AddRack()
    #cursor.close()
    #b.close()



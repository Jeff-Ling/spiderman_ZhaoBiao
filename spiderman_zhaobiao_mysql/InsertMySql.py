# -*- coding:utf-8 -*-
import MySQLdb
import time

class InsertMySql(object):
    def insert_mysql1(self, data):
        #time.sleep(5)
        #print data
        # print data['title']
        # print data['date']
        # print data['content']
        # print data['title']
        #insert_data = "(0,'时间',CURDATE(),UUID_SHORT(),(select id from app_matrix where source=1 and name='美好滁州'),'s','图片','title')"
        #测试数据库
        #con = MySQLdb.connect(host='120.195.112.176',user='root',passwd='123456',db='python_test',port=5306,charset='utf8')
        #con = MySQLdb.connect(host='47.104.128.137',user='xzly',passwd='xzly',db='xzly',port=3306,charset='utf8')
        con = MySQLdb.connect(host='47.105.85.173', user='xzly', passwd='xzly', db='xzly', port=3306, charset='utf8')
        # 生产数据库
        #con = MySQLdb.connect(host='47.104.6.174',user='caij',passwd='caij@123456',db='chuzhouTest',port=3306,charset='utf8')
        cur = con.cursor()
        #查找
        #cur.execute("select id from app_matrix where source=(select case when '微博'='微博' then '1' when '头条号'='微博' then '2'  when '企鹅号'='微博'  then '3'  end) and name = '美好滁州'")
        #res = cur.fetchall()
        #for line in res:
        #    print line
        #插入数据库
        try:
            #sql = "INSERT INTO app_matrix_article (isuse,id,accountName,create_date_time,releasetime,title,content,display_url) VALUES (0,UUID_SHORT(),%s,%s,%s,%s,%s,%s)"
            sql = "INSERT INTO zhaobiao_details (isuse,id,accountName,create_date_time,releasetime,title,content,display_url) VALUES (0,UUID_SHORT(),%s,%s,%s,%s,%s,%s)"
            # sql = "INSERT INTO app_matrix_article (isuse,releasetime,create_date_time,id,accountid,title,display_image_url,content) VALUES (0,'%s',CURDATE(),UUID_SHORT(),(select id from app_matrix where source='1' and name='美好滁州'), %s,'图片', %s)"
            param = (data['accountName'],data['date'],data['date'], data['title'], data['content'],data['url'])
            cur.execute(sql, param)
            con.commit()
            con.close()
            print ('insert successfully:'+data['title'])
            #print data
        except Exception as e:
            print (e)

    def insert_mysql(self, data):
        #time.sleep(5)

        #测试数据库
        #con = MySQLdb.connect(host='120.195.112.176',user='root',passwd='123456',db='python_test',port=5306,charset='utf8')
        # 生产数据库 01 老向数据库
        #con = MySQLdb.connect(host='47.105.85.173',user='xzly',passwd='xzly',db='tydp',port=3306,charset='utf8')
        #con = MySQLdb.connect(host='47.105.85.173', user='gldj', passwd='gldj123!@#', db='tydp', port=3306,
         #                    charset='utf8')
        con = MySQLdb.connect(host='221.229.221.35', user='root', passwd='Pj84452882?', db='pjonline', port=3306, charset='utf8')

        # 生产数据库

        #con = MySQLdb.connect(host='47.104.6.174',user='caij',passwd='caij@123456',db='chuzhouTest',port=3306,charset='utf8')
        cur = con.cursor()
        #查找
        #cur.execute("select id from app_matrix where source=(select case when '微博'='微博' then '1' when '头条号'='微博' then '2'  when '企鹅号'='微博'  then '3'  end) and name = '美好滁州'")
        #res = cur.fetchall()
        #for line in res:
        #    print line
        #插入数据库
        try:
            #判断数据库中是否已经存在
            sql1 = "select * from   zhaobiao_details  where  title = %s "    # (isUse,info,releaseTime,createTime,title,content,display_image_url) VALUES (1,%s,%s,CURDATE(),%s,%s,%s)"
            #print(data['title'])
            param1 = (data['title'],)
            print(sql1)
            count = cur.execute(sql1,param1)
            print("count:")
            print(count)
            print(data['title'])
            if count == 0:
                # #sql = "INSERT INTO app_matrix_article (isuse,id,accountName,create_date_time,releasetime,title,content,display_url) VALUES (0,UUID_SHORT(),%s,%s,%s,%s,%s,%s)"
                # sql = "INSERT INTO zhaobiao_details (isUse,info,releaseTime,createTime,title,content,display_image_url) VALUES (1,%s,%s,CURDATE(),%s,%s,%s)"
                # # sql = "INSERT INTO app_matrix_article (isuse,releasetime,create_date_time,id,accountid,title,display_image_url,content) VALUES (0,'%s',CURDATE(),UUID_SHORT(),(select id from app_matrix where source='1' and name='美好滁州'), %s,'图片', %s)"
                # param = (data['info'], data['time'], data['title'],data['content'],data['url'])

                sql = "INSERT INTO zhaobiao_details (isuse,id,accountName,createdatetime,releasetime,title,content,displayurl) VALUES (0,UUID_SHORT(),%s,CURDATE(),%s,%s,%s,%s)"
                # sql = "INSERT INTO app_matrix_article (isuse,releasetime,create_date_time,id,accountid,title,display_image_url,content) VALUES (0,'%s',CURDATE(),UUID_SHORT(),(select id from app_matrix where source='1' and name='美好滁州'), %s,'图片', %s)"
                param = (data['accountName'], data['date'], data['title'], data['content'], data['url'])

                print ("sql:"+sql)
                cur.execute(sql, param)
                con.commit()
                con.close()
                print('insert successfully')
            #print data
            else:
                print (u"data exist:"+data['title'])
        except Exception as err:
            print(err)
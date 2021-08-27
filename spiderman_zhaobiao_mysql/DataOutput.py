# coding:utf-8
import codecs
import datetime
import time
import os
#import csv
import unicodecsv as csv

class DataOutput(object):

    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    #这里要改成文件存储 待完善
    def output_html(self):
        fout=codecs.open('kuaibao_1.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        #到这个地方为址，数量是正确的，进入for循环后，数量不对了
        #print self.datas
        for data in self.datas:
            #print data['title']
            #print data['summary']
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.close

    def output_csv(self):
        # 获取当前工作目录
        os.getcwd()
        #print os.getcwd()
        # 更改当前工作目录 将文件输出到当前路径下的toutiaoOP目录
        os.chdir(os.getcwd()+'\\kuaibaoOP')
        #print os.getcwd()
        headers = ['cate','account', 'date','title', 'content','image']
        # rows = [{'url': 'https://www.toutiao.com/item/6594796352390038020/','summary': '<div><p><strong></strong></p></div>', 'title': u'\u6ec1\u5dde\u4e00\u5730\u53d1\u5e03\u5e72\u90e8\u804c\u52a1\u4efb\u514d\u901a\u77e5\uff01'}, {'url': 'https://www.toutiao.com/item/6594792431835677191/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u6ec1\u5dde\u591a\u5bb6\u5355\u4f4d\u62df\u8058\u4eba\u5458\u516c\u793a\uff01'}, {'url': 'https://www.toutiao.com/item/6594693844577550856/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u52a1\u5de5\u4eba\u5458\u7684\u5b69\u5b50\u53ef\u4ee5\u5728\u6ec1\u57ce\u4e0a\u5c0f\u5b66\u5417\uff1f\u5b98\u65b9\u56de\u590d\u2192'}, {'url': 'https://www.toutiao.com/item/6594792425342894595/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u7d27\u6025\u63d0\u9192\uff01\u4e2d\u79cb\u706b\u8f66\u7968\u5df2\u5f00\u552e\uff01\u5341\u4e00\u706b\u8f66\u79685\u5929\u540e\u5f00\u62a2\uff0c\u8fd8\u6709\u2026\u2026'}, {'url': 'https://www.toutiao.com/item/6594437583315403271/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u665a\u9910\u4e0e\u4f53\u91cd\u548c\u5bff\u547d\u7684\u5173\u7cfb\uff0c\u5e78\u597d\u4eca\u5929\u77e5\u9053\u4e86\uff01'}, {'url': 'https://www.toutiao.com/item/6594696776677065229/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u4f18\u4eb2\u539a\u53cb\uff0c\u6ec1\u5dde\u8fd97\u4eba\u88ab\u67e5\u5904\uff01'}, {'url': 'https://www.toutiao.com/item/6594693869479133710/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u4e00\u7fa4\u6ec1\u5dde\u4eba\uff0c\u8fdd\u53cd\u4ea4\u901a\u89c4\u5219\u88ab\u66dd\u5149\u4e86\uff01'}, {'url': 'https://www.toutiao.com/item/6594693914928611844/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u4f60\u4e11\u5f97\u771f\u522b\u81f4\uff01\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8'}, {'url': 'https://www.toutiao.com/item/6594693851208745480/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u6ec1\u57ce\u8fd9\u5bb6\u4e8b\u4e1a\u5355\u4f4d\u62db\u8058\uff0c\u62a5\u540d\u5df2\u5f00\u59cb\u4e86\uff01'}, {'url': 'https://www.toutiao.com/item/6594437612339986957/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u91cd\u78c5\uff01\u4e2a\u7a0e\u6cd5\u4e8c\u5ba1\u7ef4\u6301\u8d77\u5f81\u70b95000\u4e0d\u53d8\uff01\u8fd8\u6709\u4e2a\u91cd\u5927\u53d8\u5316\u2026\u2026'}, {'url': 'https://www.toutiao.com/item/6594792420003545608/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u4e0b\u4e2a\u6708\u5f00\u59cb\uff0c\u6ec1\u5dde\u8fd9\u4e9b\u666f\u533a\u96c6\u4f53\u964d\u4ef7\uff01'}, {'url': 'https://www.toutiao.com/item/6594437579314037255/', 'summary': '<div><p><strong>\xe5\x93\x88\xe5\x93\x88</strong></p></div>', 'title': u'\u6ec1\u5dde\u4e00\u56fd\u4f01\u62db\u8058\uff0c\u6708\u6536\u5165\u7ea65000\uff01'}]
        # rows = [{'url':'1','summary':'1','title':'1'},{'url':'1','summary':'2','title':'3'},{'url':'1','summary':'2','title':'3'}]
        #  rows = [{'url':'1','summary':'1','title':'1'}]
        #以日期和时间来命名csv文件
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        with open('%s_kuaibao.csv'%now, 'wb') as f:
            f.write(codecs.BOM_UTF8)    #防乱码
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            #print self.datas
            f_csv.writerows(self.datas)
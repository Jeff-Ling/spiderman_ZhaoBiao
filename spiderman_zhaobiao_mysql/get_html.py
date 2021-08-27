# coding:utf-8
#根据url数字特性，逐一遍例
#这种方法耗时太久，不可取
#尝试从下一页或上一页中获取url

import requests
from HtmlDownloader import HtmlDownloader

from urllib import urlopen

#url = 'http://www.baidu.com'




url = 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/201809/t20180904_77118.html'
#引入下载器
#downloader = HtmlDownloader()
#循环测试网址是否正确
day = 1
urls = []
url_num = 0
while (day <=31):
    print '我是day：',day
    i = 7000
    while (i <= 8000):
        print '我是i：',i
        url = 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/201809/t2018090%d_7%d.html'%(day,i)
        if day>=10:
            url = 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/201809/t201809%d_7%d.html'%(day,i)
        #url = 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/201809/t20180904_77%d.html'%i
        print url
        resp = urlopen(url)
        code = resp.getcode()

        if code == 200:
            urls.append(url)
            url_num += 1
            print urls
        print('the result is :', code)
        #print downloader.download(url)
        i += 1
    print day
    day += 1
print url_num
print urls
# 对于中国政府采购网的爬虫
# http://www.ccgp.gov.cn/cggg/

import requests
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time

# 进行分类
category = ['zygg/', 'dfgg/']
index_url = 'http://www.ccgp.gov.cn/cggg/'
root_url = 'http://www.ccgp.gov.cn/cggg/'
urls = []

for cate in category:

    cate_index_url = index_url + cate + 'index'
    cate_root_url = root_url + cate

    for i in range(0, 5):
        if (i == 0):
            current_index_url = cate_index_url + '.htm'
        else:
            current_index_url = cate_index_url + '_' + str(i) + '.htm'

        html = urlopen(current_index_url)
        bsObj = BeautifulSoup(html, 'html.parser')

        t1 = bsObj.find_all('a')
        for t2 in t1:
            t3 = str(t2.get('href'))
            if t3.startswith("./gkzb") or t3.startswith("./jzxcs"):
                t3 = t3.lstrip("./") 
                url =  cate_root_url + str(t3)
                resp = urlopen(url)
                code = resp.getcode()
                if code == 200:
                    urls.append(url)
                #print(url)

downloader = HtmlDownloader()
insertmysql = InsertMySql()

for url in urls:

    html = downloader.download(url)

    soup = BeautifulSoup(html, 'html.parser')

    #获取标题
    title = str(soup.find('title'))
    title = title.lstrip("<title>")
    title = title.rstrip("</title>")
    #print(title)

    #获取内容(Article)
    content = str(soup.find('div',class_=re.compile("vF_detail_content")))
    #print(content)
    
    #获取发布时间
    date_time = str(soup.find('span', id=re.compile("pubTime")))
    date_time = date_time.lstrip('<span id="pubTime">')
    date_time = date_time.rstrip('</span>')
    #print(date_time)

    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '中国政府采购网'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
# 对于安徽省合肥市公共资源交易平台的爬虫
# http://www.ggzy.hefei.gov.cn'

import requests
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time

# 要扒的页数
pages = 5

first_index_url = 'http://ggzy.hefei.gov.cn/jyxx/002002/002002001/moreinfo_jyxxgg2.html'
other_index_url = 'http://ggzy.hefei.gov.cn/jyxx/002002/002002001/'
root_url = 'http://ggzy.hefei.gov.cn'

urls = []

for i in range(0, pages):
    
    if (i == 0):
        current_index_url = first_index_url
    else:
        current_index_url = other_index_url + str(i + 1) + '.html'
    
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    #ret = Request(current_index_url, headers = headers)

    html = urlopen(current_index_url)
    bsObj = BeautifulSoup(html, 'html.parser')

    t1 = bsObj.find_all('a')
    for t2 in t1:
        t3 = str(t2.get('href'))
        if t3.startswith("/jyxx"):
            url =  root_url + t3
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
    title = str(soup.find('input', id = "title"))
    title = title.lstrip('<input id="title" type="hidden" value="')
    title = title.rstrip('"/>')
    if (title == "None"):
        continue
    #print(title)

    #获取内容(Article)
    content = str(soup.find_all('p',class_=re.compile("MsoNormal")))
    #print(content)
    
    #获取发布时间
    date_time = str(soup.find('input', id = "infodate"))
    date_time = date_time.lstrip('<input id="infodate" type="hidden" value="')
    date_time = date_time.rstrip('"/>')
    #print(date_time)

    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '安徽省合肥市公共资源交易中心'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
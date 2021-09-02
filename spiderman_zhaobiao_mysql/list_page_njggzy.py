# 对于 南京市公共交易资源平台 爬虫
# http://njggzy.nanjing.gov.cn/njweb/zfcg/067001/067001001/moreinfozfcg.html

import requests
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time

# 选择要扒的页数
pages = 7

first_index_url = 'http://njggzy.nanjing.gov.cn/njweb/zfcg/067001/067001001/moreinfozfcg.html'
other_index_url = 'http://njggzy.nanjing.gov.cn/njweb/zfcg/067001/067001001/'
root_url = 'http://njggzy.nanjing.gov.cn/'

urls = []

for i in range (1, pages):
    if (i == 1):
        current_index_url = first_index_url
    else:
        current_index_url = other_index_url + str(i) + '.html'

    html = urlopen(current_index_url)
    bsObj = BeautifulSoup(html, 'html.parser')

    t1 = bsObj.find_all('li')
    for t2 in t1:
        t3 = str(t2.get('onclick'))
        if (t3 != "None"):
            print(t3)
            t3 = t3.lstrip("window.open('")
            t3 = t3.rstrip("');")
            url = root_url + t3
            print(url)
            resp = urlopen(url)
            code = resp.getcode()
            if code == 200:
                urls.append(url)        

downloader = HtmlDownloader()
insertmysql = InsertMySql()

for url in urls:

    html = downloader.download(url)

    soup = BeautifulSoup(html, 'html.parser')

    #获取标题
    title = str(soup.find('div', class_=re.compile("article-info")).find('h1'))
    title = title.lstrip("<h1>")
    title = title.rstrip("</h1>")
    print(title)

    #获取内容(Article)
    content = str(soup.find('div',class_=re.compile("wz")))
    if (content == "None"):
        content = str(soup.find('div',class_=re.compile("article-info")))


    print(content)
    
    #获取发布时间
    date_time = str(soup.find('div', class_=re.compile("article-info")).find('span'))
    date_time = date_time.lstrip('<span style="font-size:14px;font-weight:bold;">\r\n\t\t\t\t\t\t\t\t\t\t【信息发布时间：')
    date_time = date_time.rstrip('】\r\n\t\t\t\t\t\t\t\t\t</span>')
    print(date_time)

    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '南京市公共资源交易中心'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
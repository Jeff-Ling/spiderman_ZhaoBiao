# 对于中招联合招标采购网的爬虫
# http://www.365trade.com.cn/zbgg/index.jhtml

import requests
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time

index_url = 'http://www.365trade.com.cn/zbgg/index'
root_url = 'http://www.365trade.com.cn'
urls = set()

# travsersal every page
for i in range(1, 5):
    current_index_url = index_url + "_" + str(i) + ".jhtml"

    html = urlopen(current_index_url)
    bsObj = BeautifulSoup(html, 'html.parser')
    t1 = bsObj.find_all('a')
    for t2 in t1:
        t3 = str(t2.get('href'))
        if t3.startswith("/zgczb") or t3.startswith("/zfwzb") or t3.startswith("/zhwzb"):
            url =  root_url + str(t3)
            resp = urlopen(url)
            code = resp.getcode()
            if code == 200:
                urls.add(url)


downloader = HtmlDownloader()
insertmysql = InsertMySql()

for url in urls:

    html = downloader.download(url)

    soup = BeautifulSoup(html, 'html.parser')

    #获取标题
    title = str(soup.find('div',class_=re.compile("container")).find('h2'))
    title = title.lstrip("<h2>")
    title = title.rstrip("</h2>")

    #获取内容(Article)
    content = str(soup.find('div',class_=re.compile("WordSection1")))
    if (content == None):
        str(soup.find('div',class_=re.compile("wrap").find_all('wrap_content')))

    #获取发布时间
    date_time = soup.find('div', class_=re.compile("container")).find_all('span')
    date_time = str(date_time[2])
    date_time = date_time.lstrip("<span>")
    date_time = date_time.rstrip("</span>")
    date_time = date_time[5:]

    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '中招联合招标采购网'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
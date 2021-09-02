# 对于解放号的爬虫
# jfh.com

import requests
import json
from urllib import request,parse
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time

urls = []
pages = 5 # 要扒的页数

root_url = 'https://www.jfh.com/purbid/workMarket/getRequestData?pageNo='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

for x in range (0, pages):
    current_url = root_url + str(x + 1)

    response = requests.get(current_url)
    if response.status_code == 200:
        json_text = response.json()
        result_list = (json_text.get('resultList'))
        for i in result_list:
            url = i['detailsUrl'] + i['orderNo']
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
    title = soup.find('div', class_=re.compile("orderextop_det"))
    if (title == None):
        continue
    else:
        title = str(title.find('h3'))
        title = title.lstrip("<h3>")
        title = title.rstrip("</h3>")
        #print(title)

    #获取内容(Article)
    content_source = soup.find('iframe', id=re.compile("myrame")).get('src')
    content_url = 'https://www.jfh.com' + str(content_source)
    content_html = downloader.download(content_url)
    content_soup = BeautifulSoup(content_html, 'html.parser')

    content = str(content_soup.find('div', id=re.compile('id_content')))


    #获取发布时间
    date_time = str(soup.find_all('span', style=re.compile("color:#8c8c8c;"))[1])
    date_time = date_time.lstrip('<span style="color:#8c8c8c;">发布时间：')
    date_time = date_time.rstrip('</span>')

    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '解放号'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
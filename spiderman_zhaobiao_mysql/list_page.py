# coding:utf-8
#此页完成了对http://www.njgp.gov.cn 南京市政府采购网的爬取、
#此网站对ip地址未做判断

#根据url数字特性，逐一遍例
#这种方法耗时太久，不可取
#尝试从下一页或上一页中获取url
#问题：通过上一页爬取，地址不好拼
#尝试先爬列表页，从列表页获取所有内容页url


import requests
from HtmlDownloader import HtmlDownloader
from InsertMySql import InsertMySql
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import Request, urlopen
import datetime
import time
#url = 'http://www.baidu.com'


#分类参数
cate_name = ['jzcgjg','bmjzcgjg','qjcgjg','shdljg']
#原始url，匹配分类参数后可以组成不同的分类地址
url = 'http://www.njgp.gov.cn/cgxx/cggg/'

#url_short = url[0:-5]
#引入下载器
#downloader = HtmlDownloader()
#循环测试网址是否正确
urls = []
url_num = 0

for cate in cate_name :
    #组成具体分类url
    cate_url = url+cate+'/'

    # Anti-Spiderman
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    ret = Request(cate_url, headers = headers)
    html = urlopen(ret)
    bsObj = BeautifulSoup(html, 'html.parser')
    t1 = bsObj.find_all('a')
    for t2 in t1:
        '''if cate == "bmjzcgjg":
            print(t2)'''
        print(t2)
        t3 = t2.get('href')
        if t3.startswith("./") and t3 != "./":
            t3 = t3[2:]
            #print(t3)

            sub_url = cate_url + t3
            #print(sub_url)

            #判断返回值 200为存在
            resp = urlopen(sub_url)
            code = resp.getcode()
            if code == 200:
                urls.append(sub_url)
                url_num += 1

    '''#print cate_url
    i = 0
    #取前i页url，南京市政府采购网，总页面比较少
    while (i <= 5):
        print ('我是i：',i)
        if i == 0:
            sub_url = cate_url
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            ret = Request('http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/', headers = headers)
            html = urlopen(ret)
            bsObj = BeautifulSoup(html, 'html.parser')
            t1 = bsObj.find_all('a')
            for t2 in t1:
                t3 = t2.get('href')
        else:
            #print url[0:-5]
            #url = url[0:-5]
            #组合出每页的url
            sub_url = cate_url+'index_%d.html'%i

            #判断返回值 200为存在
            resp = urlopen(sub_url)
            code = resp.getcode()
            if code == 200:
                urls.append(sub_url)
                url_num += 1
            i += 1'''

#print url_num
#print (urls)


#urls = ['http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_6.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_7.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_8.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_9.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_10.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_11.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_12.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_13.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_14.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_15.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_16.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_17.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_18.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_19.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_20.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_21.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_22.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_23.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_24.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_25.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_26.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_27.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_28.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_29.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_30.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_31.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_32.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_33.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_34.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/qjcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_6.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_7.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_8.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_9.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_10.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_11.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_12.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_13.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_14.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_15.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_16.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_17.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_18.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_19.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_20.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_21.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_22.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_23.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_24.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_25.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_26.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_27.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_28.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_29.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_30.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_31.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_32.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_33.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_34.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_35.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_36.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_37.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_38.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_39.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_40.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_41.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_42.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_43.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_44.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_45.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_46.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_47.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_48.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_49.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_50.html', 'http://www.njgp.gov.cn/cgxx/cggg/qtbx/']
downloader = HtmlDownloader()
insertmysql = InsertMySql()

#parent_url = 'http://www.njgp.gov.cn/cgxx/cggg/'
#sub_page_urls = []
#sub_page_num = 0
for url in urls:

    html = downloader.download(url)

    soup = BeautifulSoup(html, 'html.parser')
    #print soup.prettify()

    #获取标题
    title = soup.find('div', class_=re.compile("title")).find('h1')
    title = str(title)
    title = title.lstrip("<h1>")
    title = title.rstrip("</h1>")

    #获取内容(Article)
    content = soup.find('div',class_=re.compile("article"))
    #soup_code = BeautifulSoup(str(content), 'lxml')
    #content = soup_code.find('div', class_=re.compile("WordSection1"))
    
    #获取发布时间
    extra = soup.find('div', class_=re.compile("extra"))

    #发布时间为 date_time
    date_time = extra.get_text().strip()
    date_time = date_time[5:16]
    date_time = str(date_time).strip()
    
    today = datetime.date.today()  # 获取当天日期
    yesterday = today - datetime.timedelta(days=2)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
    yesterday = yesterday.strftime('%Y-%m-%d')

    #入库
    data = {}
    data['title'] = title
    data['date'] = date_time
    data['content'] = content
    data['url'] = url
    data['accountName'] = '南京市政府采购网'
    insertmysql.insert_mysql(data)

    print ('-----------------------------')
    
    '''soup_code = BeautifulSoup(str(links), 'lxml')
    print ("soup_code")
    print (soup_code)
    pages = soup_code.find_all('a', href=re.compile("./"))
    print ("Len: pages:")
    print (len(pages))
    #print pages
    for page in pages:
        print ("Page:")
        print (page)
        data = {}
        sub_page_url = page['href']
        #print sub_page_url
        sub_full_url = urllib.urljoin(url,sub_page_url)
        #print sub_full_url
        sub_page_urls.append(sub_full_url)
        sub_html = downloader.download(sub_full_url)
        sub_soup = BeautifulSoup(sub_html, 'lxml')
        #获取标题
        sub_links_title = sub_soup.find('div', class_=re.compile("title")).find('h1')
        #获取发布时间
        sub_date = sub_soup.find('div',class_=re.compile('extra'))
        #print sub_date
        # 获取内容详情
        sub_links_content = sub_soup.find_all('div', class_=re.compile("article"))
        title = sub_links_title.get_text()
        print (title)
        date_time = sub_date.get_text().strip()
        date_time = date_time[5:16]
        # 发布时间为 date_time
        date_time = str(date_time).strip()
        print (date_time)

        today = datetime.date.today()  # 获取当天日期
        yesterday = today - datetime.timedelta(days=2)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
        yesterday = yesterday.strftime('%Y-%m-%d')
        print("Yesterday")
        print (yesterday)
        print (type(date_time))
        print (type(yesterday))
        #date_time =str(date_time)
        #if date_time!=yesterday:  # 统一为字符串类型才好比较
        #if date_time != '2018-09-13' or date_time!='2018-09-12' or date_time!='2018-09-11' or date_time!='2018-09-10' or date_time!='2018-09-09' or date_time!='2018-09-08':
        if date_time < '2018-11-02':       #20181102
            print ('-------date not match-------')
            continue


        #print date_time
        content = sub_links_content
        #print content[0]
        data['title'] = title
        data['date'] = date_time
        data['content'] = content[0]
        data['url'] = sub_full_url
        data['accountName'] = '南京市政府采购网'
        #print data
        #入库
        insertmysql.insert_mysql(data)
        #title = page.get_text()
        #print title
        sub_page_num += 1'''

#print sub_page_urls
#print (sub_page_num)
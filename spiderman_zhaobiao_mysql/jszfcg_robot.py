# coding:utf-8
#此页完成了对http://www.ccgp-jiangsu.gov.cn 江苏政府采购网的爬
#此网站对ip地址未做判断,不需要设定延时

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
import urlparse
from urllib import urlopen
import datetime
import time

#分类参数
#cate_name = ['jzcgjg','bmjzcgjg','qjcgjg','shdljg','qtbx']
#原始url，匹配分类参数后可以组成不同的分类地址
url = 'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/'

#url_short = url[0:-5]
#引入下载器
#downloader = HtmlDownloader()
#循环测试网址是否正确
urls = []
url_num = 0

#for cate in cate_name :
    #组成具体分类url
#    cate_url = url+cate+'/'
    #print cate_url
i = 0
#取前i页url，南京市政府采购网，总页面比较少
while (i <= 5):
    print '我是i：',i
    if i == 0:
        sub_url = url
    else:
        #print url[0:-5]
        #url = url[0:-5]
        #组合出每页的url
        sub_url = url+'index_%d.html'%i
        print sub_url
    #判断返回值 200为存在
    resp = urlopen(sub_url)
    code = resp.getcode()
    print code
    if code == 200:
        urls.append(sub_url)
        url_num += 1
    i += 1



print url_num
print urls


#urls = ['http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_6.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_7.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_8.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_9.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_10.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_11.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_12.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_13.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_14.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_15.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_16.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_17.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_18.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_19.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_20.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_21.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_22.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_23.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_24.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_25.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_26.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_27.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_28.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_29.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_30.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_31.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_32.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_33.html', 'http://www.njgp.gov.cn/cgxx/cggg/jzcgjg/index_34.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/bmjzcgjg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/qjcgjg/', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_1.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_2.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_3.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_4.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_5.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_6.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_7.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_8.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_9.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_10.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_11.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_12.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_13.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_14.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_15.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_16.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_17.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_18.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_19.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_20.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_21.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_22.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_23.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_24.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_25.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_26.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_27.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_28.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_29.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_30.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_31.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_32.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_33.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_34.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_35.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_36.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_37.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_38.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_39.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_40.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_41.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_42.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_43.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_44.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_45.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_46.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_47.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_48.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_49.html', 'http://www.njgp.gov.cn/cgxx/cggg/shdljg/index_50.html', 'http://www.njgp.gov.cn/cgxx/cggg/qtbx/']
downloader = HtmlDownloader()
insertmysql = InsertMySql()

#parent_url = 'http://www.njgp.gov.cn/cgxx/cggg/'

sub_page_urls = []
sub_page_num = 0
for url in urls:
    #print url
    html = downloader.download(url)
    #print html

    soup = BeautifulSoup(html, 'lxml')
    #print soup.prettify()
    links = soup.find_all('div',class_=re.compile("list_list"))
    #print links
    soup_code = BeautifulSoup(str(links), 'lxml')
    pages = soup_code.find_all('a', href=re.compile("./"))
    print pages
    for page in pages:
        #print page
        data = {}
        sub_page_url = page['href']
        #print sub_page_url
        sub_full_url = urlparse.urljoin(url,sub_page_url)
        print sub_full_url
        sub_page_urls.append(sub_full_url)
        sub_html = downloader.download(sub_full_url)
        sub_soup = BeautifulSoup(sub_html, 'lxml')
        #获取标题
        sub_links_title = sub_soup.find('div', class_=re.compile("dtit")).find('h1')
        #获取发布时间
        sub_date = sub_soup.find('span',class_=re.compile('mid'))
        print sub_date
        title = sub_links_title.get_text().strip()
        print title
        date_time = sub_date.get_text().strip()
        date_time = date_time[6:16]
        print date_time
        # 发布时间为 date_time
        date_time = str(date_time).strip()
        print date_time

        today = datetime.date.today()  # 获取当天日期
        yesterday = today - datetime.timedelta(days=2)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
        yesterday = yesterday.strftime('%Y-%m-%d')
        print yesterday
        print type(date_time)
        print type(yesterday)
        #date_time =str(date_time)
        #if date_time!=yesterday:  # 统一为字符串类型才好比较
        #if date_time != '2018-09-13' or date_time!='2018-09-12' or date_time!='2018-09-11' or date_time!='2018-09-10' or date_time!='2018-09-09' or date_time!='2018-09-08':
        if date_time < '2018-11-02':    #20181102
            print '-------date not match-------'
            continue

        # 获取内容详情
        sub_links_content = sub_soup.find_all('div', class_=re.compile("detail_con"))
        #print date_time
        content = sub_links_content
        #print content[0]
        data['title'] = title
        data['date'] = date_time
        data['content'] = content[0]
        data['url'] = sub_full_url
        data['accountName'] = '江苏政府采购网'
        #print data
        #入库
        insertmysql.insert_mysql(data)
        #title = page.get_text()
        #print title
        sub_page_num += 1

    print '-----------------------------'
#print sub_page_urls
print sub_page_num

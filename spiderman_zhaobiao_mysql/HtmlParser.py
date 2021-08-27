# coding:utf-8
import re
import time
import urlparse
import datetime
import HtmlParser
import lxml
from bs4 import BeautifulSoup
from InsertMySql import InsertMySql
from HtmlDownloader import HtmlDownloader

class HtmlParser(object):
    def get_data(self,html):
        '''
        抽取新的url集合
        :param page_url: 下载页的url
        :param soup: soup
        :return: 返回新的url集合
        '''
        soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
        print soup.prettify()
        new_urls = set()
        #抽取符合要求的a标签
        #links = soup.find_all('a',class_=re.compile("_37Q9mExSDMg6UKq5g0-GhX"))

        #links = soup.find_all('a', href=re.compile("details")) #选出可用的链接，注意这个链接是不全的，需要补全
        all_code = soup.find_all('a', class_=re.compile("_37Q9mExSDMg6UKq5g0-GhX"))
        print all_code
        num = 0
        for code in all_code:
            #print type(code)
            print code
            soup_code = BeautifulSoup(str(code),'lxml')
            release_date = soup_code.find('span',class_=re.compile("_26elxhEbCxuVKq0_S0xwRS"))
            print release_date
            #判断时间
            release_date = release_date.get_text().split(' ')  # 分割日期和时间
            print release_date
            print type(release_date)
            release_date = release_date[0]  # 获得日期
            print type(release_date)
            #release_date = str(release_date)
            print release_date
            #日期是中文的，分别拿出月份和日期
            #release_date = release_date.split('月')
            #print release_date
            release_month = release_date[0:1]    #取出月份    10 11 12月要单独处理
            release_day = release_date[2:4]      #取出天
            release_date = '2018-0'+release_month+'-'+release_day
            print release_date
            #print release_date[0]
            #print type(release_date)
            today = datetime.date.today()  # 获取当天日期
            yesterday = today - datetime.timedelta(days=1)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
            yesterday = yesterday.strftime('%Y-%m-%d')
            print yesterday
            #print type(yesterday)
            # if data['time']!='2018-08-28 14:39':
            if release_date != yesterday:  # 统一为字符串类型才好比较
                print 'Time not match!!!!'
                continue
            print 'Time match'
            #print release_date
            links = soup_code.find('a', class_=re.compile("_37Q9mExSDMg6UKq5g0-GhX"))
            print links
            new_url = links['href']
            print new_url
            # 取文章链接
            #print new_url
            new_full_url = urlparse.urljoin(page_url, new_url)
            print new_full_url
            # 直接解析的取数据并入库
            time.sleep(4)
            self.downloader = HtmlDownloader()
            html = self.downloader.download(new_full_url)
            #print html
            soup = BeautifulSoup(html, 'lxml')

            data = {}
            # data={'cate','account','date','title','content','image'}
            # 账号类型
            data['cate'] = '头条号'
            # 账号名称
            account = soup.find('span', class_=re.compile("author"))
            data['account'] = account.get_text()
            # print soup    #头条号程序加载的html和F12中看到的不一定一样，以加载的为准
            #日期
            data['date'] = yesterday
            # 标题
            title = soup.find('p', class_=re.compile("title"))
            data['title'] = title.get_text().strip()  # strip()去除所有空格
            print data['title']
            # 内容
            content = soup.find('div', class_='content-box')
            # data['summary'] = 'u\''+summary+'\''    #这样不行 summary 是object 先把object转str
            content = str(content)  # object转为string
            data['content'] = content.decode(
                'utf-8')  # string 转为unicode 参考网址：https://blog.csdn.net/vbaspdelphi/article/details/60332613
            # 图片
            # 只取一张图片，没有不取
            data['image'] = ''
            image = soup.find('img', style=re.compile("display:block;"))  # 这里要写成style，不是style_
            # print image
            # print type(image)
            # print image['src']
            # print type(image['src'])
            if image:  # any(object) 判断object是否为空，返回true flase
                print '----有插图----'
                data['image'] = image['src']

            self.mysql = InsertMySql()
            self.mysql.insert_mysql(data)
            num +=1
        return num



    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的url
        :param soup:
        :return: 返回有效数据
        '''
        data={}
        #data={'cate','account','date','title','content','image'}
        #账号类型
        data['cate'] = '企鹅号'
        #账号名称
        account = soup.find('span',class_=re.compile("author"))
        data['account']= account.get_text()
        print data['account']
        #发布时间    后面要根据日期判断，只抓取前一天的
        time = soup.find('span',class_=re.compile("time"))
        time = time.get_text().split(' ')    #分割日期和时间
        date = time[0]    #获得日期
        today=datetime.date.today()    #获取当天日期
        yesterday = today - datetime.timedelta(days=1)  # 用今天日期减掉时间差，参数为1天，获得昨天的日期
        yesterday = yesterday.strftime('%Y-%m-%d')
        #if data['time']!='2018-08-28 14:39':
        if date!=yesterday:    #统一为字符串类型才好比较
            return
        data['date']=date
        #标题
        #title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        title = soup.find('p', class_=re.compile("title"))
        data['title']=title.get_text().strip()    #strip()去除所有空格
        print data['title']
        #内容
        content = soup.find('div',class_='content-box')
        #data['summary'] = 'u\''+summary+'\''    #这样不行 summary 是object 先把object转str
        content = str(content)    #object转为string
        data['content'] = content.decode('utf-8')    #string 转为unicode 参考网址：https://blog.csdn.net/vbaspdelphi/article/details/60332613
        #图片
        #只取一张图片，没有不取
        data['image']=''
        image = soup.find('img', style=re.compile("display:block;"))  # 这里要写成style，不是style_
        #print image
        #print type(image)
        #print image['src']
        #print type(image['src'])
        if image:  # any(object) 判断object是否为空，返回true flase
            print '----有插图----'
            data['image'] = image['src']
        '''
        取多张图片
        images = soup.find_all('img',style=re.compile("display:block;"))    #这里要写成style，不是style_
        print images
        if any(images):    #any(object) 判断object是否为空，返回true flase
            image_bank = set()
            for img in images:
                # 提取src属性
                #image = image+','+img['src']
                image = img['src']
                image_bank.add(image)
                #print image
                print image_bank
            for img in image_bank:
                rel_imgs = img['img']
                print rel_imgs
        '''
        #data['summary'] = 'summary'
        #print data['image']
        return data
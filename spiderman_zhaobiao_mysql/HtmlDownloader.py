# coding:utf-8
import requests
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        #如何加入代理 待完善
        user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
        #user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        headers = {'User-Agent':user_agent,'Connection': 'close'}
        r = requests.get(url,headers=headers)
        #return r.status_code


        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None


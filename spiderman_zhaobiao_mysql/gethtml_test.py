# coding:utf-8
import requests

# coding:utf-8
#此页完成了对http://hzjg.hua-jie.top/app/jgaa/servo 杭州江干区
#此网站对ip地址未做判断




url = 'https://www.toutiao.com/item/6594796352390038020/'
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
#user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url,headers=headers)
if r.status_code==200:
    r.encoding='utf-8'
    html = r.text
    print html
    with open("1234.txt", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(html)

print("下载成功")
#okokanyway
#简单爬虫1
import urllib2

url='  '
request=urllib2.request(url)
response=urllib2.urlopen(request).read()
print (response）
       
#简单爬虫2
import urllib2
def download(url)：
    return urllib2.urlopen(url).read()
    
#下面是加入了报错提示重新加载2次
def download(url,num_retries=2)：
    print("Doenloading",url)
    try：
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e：
        print ("Download error:",e.reason)
        html=none
        if num_retries>0:
            if hasattr (e,'code') and 500 <= e.code <600:
            return download(url,num_retries-1)
    return html

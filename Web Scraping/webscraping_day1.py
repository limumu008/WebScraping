# Install requests: pip install requests
import requests
# 1. Make a requests
#r = requests.get('https://www.baidu.com/')
# r is a Response [200]
# 2. Print the content of response
#print(r.text)
# HTTP POST request
#r = requests.post('https://www.baidu.com/')
# r is a Response [302]

# what is the headers?
# 在爬虫的时候，如果不添加请求头，可能网站会阻止一个用户的登陆，此时我们就需要添加请求头来进行模拟伪装，使用python添加请求头方法如下：
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

r = requests.get('https://www.baidu.com/', headers = headers)

print(r.text)

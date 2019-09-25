# What a new day, let's start to learn beautifulsoup.
# Task: 学习beautifulsoup，并使用beautifulsoup提取内容。
#       使用beautifulsoup提取下面丁香园论坛的特定帖子的所有回复内容，以及回复人的信息。
import re, requests
from bs4 import BeautifulSoup
url = 'http://cardiovascular.dxy.cn/bbs/topic/509959?ppg=1'
#cookies = dict([l.split("=",1)for l in cookie.split(":")])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(url, headers = headers)
#print(r.text)

# 主要处理的是4个objects: Tag, NavigableString, BeutifulSoup, and Comment.
soup = BeautifulSoup(r.text,'lxml')
#Tag,Tag name,Attribute,All attributs
soup.link,soup.link.name,soup.link['media'],soup.link.attrs
#NavigableString, replace one string with another
soup.title.string, soup.title.string.replace_with
#BeautifulSoup
soup.name
#Comment--就是html里面的comment !----我是comment---
# .contents --向下一层到child, .children--指下一层所有child
# .parent --向上一层到child, .parents--指上一层所有child
# .next_sibling 和 .previous_sibling
def parse_html(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie': 'DXY_USER_GROUP=90; __auc=dbbdcb831693f2263d8b634e48e; __utmz=1.1551542416.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JUTE_SESSION_ID=183a9354-8a7e-45e3-b0ad-dc4168d67495; JUTE_TOKEN=e49fed53-e004-49f8-b9a9-2f592f166e6a; __utmc=1; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1551542416,1551663857; CMSSESSIONID=CE09D9380FDE910715DF42FF533CE50E-n2; __utma=1.563046533.1551542416.1551664853.1551667549.8; cms_token=70f0fb8c-c354-4aef-ad00-848fdbf9df5b; __asc=aa9c736416946eee7ad1c91269f; _ga=GA1.2.563046533.1551542416; _gid=GA1.2.1499786245.1551673271; Hm_lpvt_8a6dad3652ee53a288a11ca184581908=1551673721; JUTE_SESSION=f3bbfb9fd2d17d34ea158ee4ee12f58aa17f77ca04bc3eba4c10cafea1e5e973e8a36ebcf58eac0c; __utmb=1.15.6.1551674604919'}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text,'lxml')
    # 回复结果
    replies = {}
    # 回复人
    ids = []
    for reply_id in soup.find_all("div","auth"):
        ids.append(reply_id.a.contents[0])
    # 回复内容
    reply_conts = []
    for rid, reply_cont in enumerate(soup.find_all("td","postbody")):
        temp = ""
        for content in reply_cont.contents:
            # 过滤掉</br>和<a> 并去掉空格
            if content.name!='br' and content.name!='a':
                temp+=content.strip()
            # tag<a> 包含网址信息， 所以单独考虑
            elif content.name == 'a':
                temp+=content['href']
        replies[ids[rid]] = temp
# 结果显示{'回复人1': '回复内容1'， '回复人2'：'回复内容2'}
    return replies
replies = parse_html(url)
for key in replies.keys():
    print('回复人：'+key+'\n回复内容：'+ replies[key]) 



# Task: 学习什么是IP，为什么会出现IP被封，如何应对IP被封的问题。
# 抓取西刺代理，并构建自己的代理池。
# 西刺代理 https://www.xicidaili.com/

# 1. IP, Internet Protocol, 用来与其他电脑联络的地址.
# 2. IP被封常被认为是自我保护，组织外部攻击。原因也有可能是virus, malware or spam导致的。
# 3. 爬虫之前最好使用代理IP。如果IP被封，可以重启路由器。或者购买新的IP。

import requests, re, time
from lxml import etree
#url = "https://www.xicidaili.com/nn"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
def get_html(url):
    r = requests.get(url, headers = headers)
    html = etree.HTML(r.text)
    return html

def parse_html(html):
    ip_info = html.xpath('//tr[@class="odd"]/td/text()|//tr[@class=""]/td/text()')
    address = []
    for ip in ip_info:
        if re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',ip):  
            address.append(ip)
    return address

def ip_confirm(ip):
    # 确认ip 可否使用
    try:
        requests.get('http://www.baidu.com', proxies={"http":"http://%s" %ip})
    except:
        print('failed')
    else:
        return 'true'

address = []
ip_pool= []
for i in range(1,2):
    url = "https://www.xicidaili.com/"
    html = get_html(url)
    address += parse_html(html)

for ip in address:
    if ip_confirm(ip)=='true':
        ip_pool.append(ip)
print(ip_pool)
#if __init__==__main__:
#    get_html(url)

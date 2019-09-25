# Task: 学习xpath，使用lxml+xpath提取内容。
#       使用xpath提取丁香园论坛的回复内容。

from lxml import etree
import requests
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# 利用etree.HTML初始化
html = etree.HTML(text)
#print(html)
# 再利用etree.tostring打印出来，lxml有自动修正html代码的功能，输出结果补全了最后的</li>
# 还添加了body, html标签, 输出类型是bytes
# 路径表达式
# /从根节点选取， //li 选取所有li子元素， 
# .选取当前节点， ..选取当前节点的父节点，@选取attribute
result = etree.tostring(html)
result = html.xpath('//li')

# 谓语（Predicates）
# 用来查找某个特定的节点或者包含某个指定的值的节点，常被嵌在方括号中。
# //li[1] 第一个li元素， //[last()] 最后一个li元素， //[last()-1]倒数第二个元素
# //li[position()<3] 选取最前面的两个li元素
#print(result[0])

# 选取未知节点
# * 匹配任何元素节点， @*匹配任何属性节点，
# node() 匹配任何类型的节点
# //* 选取文档中的所有元素， //title[@*]选取所有带有属性的title元素

# 选取若干路径
# | 可以理解为并且的意思， //li|//a


url = "http://www.dxy.cn/bbs/thread/626626#626626"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(url, headers = headers, timeout = 3)
html = etree.HTML(r.text)
# 回复人
repliers = html.xpath('//div[@class="auth"]/a/text()')
# 回复内容
infos = []
for i in range(1,len(repliers)+1):
    p = "post_"+str(i)
    reply_info = html.xpath('//div[@id="'+p+'"]//td[@class="postbody"]/text()')
    info = ""
    for reply in reply_info:
        info+=reply.strip()
    infos.append(info)
for i in range(len(repliers)):
    print('回复人:'+ repliers[i]+'\n回复内容：'+infos[i])
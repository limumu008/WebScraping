import requests
from lxml import etree


def get_html(url):
    headers ={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
    }

    res = requests.get(url,headers = headers)
    res.encoding = res.apparent_encoding
    return res.text
    # print(res.text)



def parse_html(res):
    data =[]
    new_data =[]
    html = etree.HTML(res)
    result_name = html.xpath('//div[@class="auth"]/a/text()')
    result_data = html.xpath('//td[@class="postbody"]/text()')
    for i in range(0,int(len(result_name))):
        data.append(result_name[i]+"++++++++"+result_data[i])

    for i in data:
        new =i.replace("\n","").replace("\t","").replace(" ","")
        new_data.append(new)
        print(new_data)
parse_html()
    
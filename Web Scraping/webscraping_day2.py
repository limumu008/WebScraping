# Today, we start to learn regular expression (regex) under re module.
# You can specify the rules for the set of possible strings that you want to match.
# 1. Matching Characters
import re
import requests

url = 'https://movie.douban.com/top250'
headers = {'Host': 'movie.douban.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# 添加请求头，防止访问网页失败
r = requests.get(url, headers = headers)
data = r.text
#print(data)
# 电影排名pattern, 注意<em class="">
ranking_pattern = re.compile(r' <em class="">(.*?)</em>')
# 设置一个pattern查找电影
pattern = re.compile(r'<div class="hd">([\d\D]*?)</li>')
# 获取每一部电影
films = pattern.findall(data)
# 设置一个查找电影名的pattern
title_pattern = re.compile(r'<span class="title">([\d\D]*?)</span>')
#for film in films:
    #print(title_pattern.findall(film))
"""
['肖申克的救赎', '&nbsp;/&nbsp;The Shawshank Redemption']
['霸王别姬']
['这个杀手不太冷', '&nbsp;/&nbsp;Léon']
['阿甘正传', '&nbsp;/&nbsp;Forrest Gump']
['美丽人生', '&nbsp;/&nbsp;La vita è bella']
['泰坦尼克号', '&nbsp;/&nbsp;Titanic']
['千与千寻', '&nbsp;/&nbsp;千と千尋の神  し']
['辛德勒的名单', '&nbsp;/&nbsp;Schindler&#39;s List']
['盗梦空间', '&nbsp;/&nbsp;Inception']
['忠犬八公的故事', '&nbsp;/&nbsp;Hachi: A Dog&#39;s Tale']
['机器人总动员', '&nbsp;/&nbsp;WALL·E']
['三傻大闹宝莱坞', '&nbsp;/&nbsp;3 Idiots']
['海上钢琴师', '&nbsp;/&nbsp;La leggenda del pianista sull&#39;oceano']
['放牛班的春天', '&nbsp;/&nbsp;Les choristes']
['楚门的世界', '&nbsp;/&nbsp;The Truman Show']
['大话西游之大圣娶亲', '&nbsp;/&nbsp;西  記大結局之仙履奇緣']
['星际穿越', '&nbsp;/&nbsp;Interstellar']
['龙猫', '&nbsp;/&nbsp;となりのトトロ']
['教父', '&nbsp;/&nbsp;The Godfather']
['熔炉', '&nbsp;/&nbsp;도가니']
['无间道', '&nbsp;/&nbsp;無間道']
['疯狂动物城', '&nbsp;/&nbsp;Zootopia']
['当幸福来敲门', '&nbsp;/&nbsp;The Pursuit of Happyness']
['怦然心动', '&nbsp;/&nbsp;Flipped']
['触不可及', '&nbsp;/&nbsp;Intouchables']
"""
# 返回第一页所有top25电影名
# 设置一个查找排名的pattern
#ranking_pattern = re.compile(r'<em class>([\d\D]*?)</em>')
country_pattern = re.compile(r'&nbsp;/&nbsp;([\d\D]*?)&nbsp;/&nbsp;')
director_pattern = re.compile(r'导演:([\d\D]*?);&nbsp;&nbsp;主演')

def one_page(url):
    """查询一页电影信息"""
    headers = {'Host': 'movie.douban.com','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    r = requests.get(url, headers = headers)
    data = r.text
    
    # pattern 包括 名次，影片名称，国家，导演
    rankList = re.findall(r'<em class="">(.*?)</em>',data)
    names = re.findall(r'<span class="title">([\d\D]*?)</span>',data)
    countries = re.findall(r'&nbsp;/&nbsp;([\u4e00-\u9fa5 ]*?)&nbsp;/&nbsp;',data)
    directors = re.findall(r'导演: (.*?)&nbsp;&nbsp;',data)

    nameList = []
    countryList = []
    directorList = []
    movieList = []
    # 匹配电影的中文名
    for name in names:
        if name.find('/') == -1:
            nameList.append(name)
    for country in countries:
        countryList.append(country)
    for director in directors:
        directorList.append(director)
    for i in range(len(rankList)):
        movieList.append((rankList[i],nameList[i],directorList[i],countryList[i]))
    return movieList


movies = []

# 豆瓣top250 movies的爬取 每页25部电影 总计10页
for page in range(8):
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    movies.append(one_page(url))
for movie in movies:
    for each_one in movie:
        print(each_one)
  


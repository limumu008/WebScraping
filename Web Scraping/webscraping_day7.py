# 实战大项目：模拟登录丁香园，并抓取论坛页面所有的人员基本信息与回复帖子内容。
# 因为没有国内手机号无法注册丁香园，改为一亩三分地。
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,re,requests
from lxml import etree

def logIn(driver):
    # 登陆命令，找到登陆账号密码位置并填入信息登陆    
    name = driver.find_element_by_id("ls_username")
    name.clear()
    name.send_keys("l******")
    pw = driver.find_element_by_id("ls_password")
    pw.clear()
    pw.send_keys("L*******")
    driver.find_element_by_tag_name("button").click()
    time.sleep(2)
def searchIn(driver):
    # 尝试使用搜索行，因为积分不够，无法搜索
    elem = driver.find_element_by_name("srchtxt")
    elem.clear()
    elem.send_keys("indeed 内推")
    elem.send_keys(Keys.RETURN)
    #assert "No results found." not in driver.page_source
def refer(driver):
    driver.find_element_by_xpath('//a[@href="forum-198-1.html"]').click()
def collectComts(driver):
    # 收集当前页面回复人和回复信息
    comt = []
    rep = []
    comments = driver.find_elements_by_xpath('//td[@class="t_f"]')
    replyers = driver.find_elements_by_xpath('//div[@class="authi"]/a[@class="xi2"]')
    for comment in comments:
        comt.append(comment.text.replace('\n',''))
    for replyer in replyers:
        rep.append(replyer.text)
    return rep, comt
def tearDown(driver):
    # 关闭网页
    driver.close()

driver = webdriver.Chrome()
# 总计4页回复，设置i的range为{1，4}
for i in range(1,5):
    replyer = []
    comment = []
    html = "https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=454793&extra=page%3D1%26filter%3Dsortid%26sortid%3D192%26sortid%3D192&page="+str(i) 
    driver.get(html)
    time.sleep(1)
    # 只有首页需要登陆账号
    if i == 1:
        logIn(driver)
    replyer,comment = collectComts(driver)
    # 返回回复人及回复内容
    for i in range(len(replyer)):
        print('回复人：'+replyer[i]+'\n回复内容：'+comment[i])
time.sleep(5)
tearDown(driver)

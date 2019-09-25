# Task: 安装selenium并学习。
# pip install selenium
# 使用selenium模拟登陆163邮箱。
import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # 如果没有chrome drive，需要下载并安装在文件同一路径
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        # 确认标题是否包含"Python"
        #assert "Python" in driver.title
        self.assertIn("Python",driver.title)
        # 查询页面中的元素 find_element_by_*
        elem = driver.find_element_by_name("q")
        # 发送一个关键字并且查询
        #elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source 
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main() """

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # 如果没有chrome drive，需要下载并安装在文件同一路径
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://mail.163.com/")
        self.assertIn("163",driver.title)
        # 为了识别各元素，需要切换到frame中.
        #driver.switch_to_frame('x-URS-iframe')
        # 查询页面中的元素 find_element_by_*
        #elem = driver.find_element_by_id("q")
        # 发送一个关键字并且查询
        #elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source 
    def tearDown(self):
        self.driver.close()
"""if __name__ == "__main__":
    unittest.main()"""

driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
time.sleep(10)
 # 为了识别各元素，需要切换到frame中.
driver.switch_to.frame(0)
# 定位账号输入口
name = driver.find_element_by_name("email")
# 每次输入账号前 记得clear
name.clear()
# 发送用户名
name.send_keys("l*****8")
# 定位密码输入口
pw = driver.find_element_by_name("password")
pw.clear()
# 发送密码
pw.send_keys("L*****")
# 定位登陆键并点击
driver.find_element_by_id("dologin").click()
time.sleep(2)
#跳出frame， 回归主页面
driver.switch_to_default_content()

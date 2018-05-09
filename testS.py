import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# seleniumTest.py和同样的功能，我们将其封装为测试标准类的形式。

class PythonOrgSearch(unittest.TestCase):
    # 测试用例是继承了 unittest.TestCase 类，继承这个类表明这是一个测试类
    def setUp(self):
        self.driver = webdriver.Chrome()
    # setUp方法是初始化的方法，这个方法会在每个测试类中自动调用。每一个测试方法命名都有规范，必须以 test 开头，会自动执行。

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
# tearDown 方法会在每一个测试方法结束之后调用。这相当于最后的析构方法。send_keys
# 在这个方法里写的是 close 方法，你还可以写 quit 方法。
# 不过 close 方法相当于关闭了这个 TAB 选项卡，然而 quit 是退出了整个浏览器。
# 当你只开启了一个 TAB 选项卡的时候，关闭的时候也会将整个浏览器关闭。


if __name__ == "__main__":
    unittest.main()
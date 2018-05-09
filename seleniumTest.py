from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
# 打开网页
assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# 通过寻找 'q' 这个搜索框
# 而且你在用 xpath 的时候还需要注意的是，如果有多个元素匹配了 xpath，它只会返回第一个匹配的元素。
# 如果没有找到，那么会抛出 NoSuchElementException 的异常。
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

# elem.send_keys("and some", Keys.ARROW_DOWN)
# 然后我们模拟了键盘的回撤点击,key这个类可以模拟键盘输入
# print (driver.page_source)
# 获取网页渲染后的属性了



# driver2 = webdriver.Chrome()
# driver2.get("http://www.baidu.com/")
# elem2 = driver2.find_element_by_name("wd")
# elem2.send_keys("chenzuo")
# elem2.send_keys(Keys.RETURN)

# 下拉选项卡的的处理可以如下
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
#根据索引来选择，可以根据值来选择，可以根据文字来选择

select = Select(driver.find_element_by_id('id'))
select.deselect_all()
# 全部取消

select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options

# 元素拖拽
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


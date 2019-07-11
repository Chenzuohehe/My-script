 # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# 控制浏览器自动操作
import time


waitSec = 16

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://www.remomo.info/pv_web_v3/dist/index.html")


# driver.find_element_by_xpath("//*[@class='button small blue submit ']").click()

driver.find_element_by_name("email").send_keys("yuekuan.zhou@connect.polyu.hk")

driver.find_element_by_name("password").send_keys("123456")

driver.find_element_by_xpath("//*[@class='MuiButton-label-125']").click()

time.sleep(waitSec)
# style="cursor: pointer;
driver.find_element_by_xpath("//*[@style='cursor: pointer;']").click()

# class="MuiTypography-root-28 MuiTypography-h4-43"

# class="MuiTypography-root-28 MuiTypography-h4-43"

lis = driver.find_element_by_xpath("//*[@class='MuiTypography-root-28 MuiTypography-h4-43']")
print(lis)

time.sleep(waitSec * 10)
driver.close()



# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# 控制浏览器自动操作
import time
# sleep

# 目标苹果开发者账户然后创建证书，添加UDID，添加B ID，生成配置文件


appleID = ""
password = ""
CRSfilePath = "/Users/chenzuo/Desktop/CertificateSigningRequest.certSigningRequest"
appName = ""
aName = ""
bundleID = "com." + appName + "." + aName
appChineseName = ""
udids = [""]

waitSec = 6

driver = webdriver.Chrome()

# browser = webdriver.Safari()
# browser.get('http://weibo.com')


# 登录开发者账号
def login():
    # 隐式等待 全局的
    driver.implicitly_wait(30)
    driver.get(
        "https://idmsa.apple.com/IDMSWebAuth/login?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Faccount%2F&rv=1")
    elem = driver.find_element_by_id("accountname")
    elem.send_keys(appleID)

    elem = driver.find_element_by_id("accountpassword")
    elem.send_keys(password)

    elem.send_keys(Keys.RETURN)
    # 自动登录OK
    time.sleep(waitSec)

# 打开CIP
def openCIP():
    driver.find_element_by_xpath("//*[@data-menu-option='cip']").click()
    # 找到CIP  Certificates, IDs & Profiles 点击
    time.sleep(waitSec)

# 创建证书 index: 0：开发证书 1：开发推送证书 2：生成发布证书 3：发布推送证书
def ceartCeetificates(index):
    driver.find_element_by_xpath("//*[@data-reactid='.0.1.0.1.0.0.0.2.1:$0.$ProgramBlock_0.2.$0.$0.0']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='toolbar-button add ']").click()
    # +添加按钮

    time.sleep(waitSec)
    radios = driver.find_elements_by_class_name("validate")
    radios[index].click()
    driver.find_element_by_xpath("//*[@class='button small blue submit ']").click()
    # 选择证书类型 and continue
    if index == 1 or index == 3:
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='button small blue submit ']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue submit ']").click()
    # 继续 continue

    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@name='upload']").send_keys(CRSfilePath)
    driver.find_element_by_xpath("//*[@class='button small blue submit ']").click()
    # CSR文件上传成功 继续

    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue']").click()
    # 下载
    driver.find_element_by_xpath("//*[@class='subitem selected']").click()
    # done
    time.sleep(waitSec)

# 创建APP ID
def creatAppId():
    driver.find_element_by_xpath("//*[@data-reactid='.0.1.0.1.0.0.0.2.1:$0.$ProgramBlock_2.2.$5']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='toolbar-button add']").click()
    # +添加按钮
    time.sleep(waitSec)
    driver.find_element_by_name("appIdName").send_keys(appName)
    driver.find_element_by_name("explicitIdentifier").send_keys(bundleID)
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue right']").click()
    # 输入APPID bundleid 继续
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue right']").click()
    # register
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small right']").click()
    # done

# 添加设备UDID
def addDevices():
    # 因为设备不能重复注册，这边就默认是好的吧，实际使用的时候再细调
    for path in udids:
        driver.find_element_by_xpath("//*[@data-link='/account/ios/device/']").click()
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='toolbar-button add']").click()
        time.sleep(waitSec)
        driver.find_elements_by_name("register")[1].click()
        time.sleep(waitSec)
        driver.find_element_by_name("upload").send_keys(path)
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='button small right navLink']").click()

# 生成配置文件 index 0：开发配置文件 4：hoc配置文件 2：生产配置文件
def addProfiles(index):
    driver.find_element_by_xpath("//*[@data-link='/account/ios/profile/']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='toolbar-button add']").click()
    time.sleep(waitSec)
    elems = driver.find_elements_by_xpath("//*[@type='radio']")
    elems[index].click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
    # 这边是默认只有一个appid
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
    time.sleep(waitSec)
    if index == 2 or index == 4:
        driver.find_element_by_xpath("//*[@name='certificateIds']").click()
    elif index == 0:
        driver.find_element_by_xpath("//*[@id='selectAllCId']").click()

    driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
    time.sleep(waitSec)

    if index == 0 or index == 4:
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@id='selectAllDId']").click()
        time.sleep(waitSec)
        driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()


    time.sleep(waitSec)
    suffix = ""
    if index == 0:
        suffix = "_dev"
    elif index == 2:
        suffix = "_dis"
    elif index == 4:
        suffix = "_hoc"
    driver.find_element_by_name("provisioningProfileName").send_keys(aName + suffix)
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue right submit']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button small blue']").click()
    # 下载
    driver.find_element_by_xpath("//*[@class='subitem selected']").click()
    # done
    time.sleep(waitSec)


# 打开iTunesConnect
def openiTunesConnect():
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@data-menu-option='itunes-connect']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='button-3d-blue font-semibold']").click()

#
def openiTunesType(index):
    time.sleep(waitSec)
    driver.get("https://itunesconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app")
    time.sleep(waitSec)

# 添加新APP
def addNewApp():
    time.sleep(waitSec)

    # 一般这边很慢需要更多的加载时间
    driver.find_element_by_xpath("//*[@class='new-button ng-isolate-scope']").click()
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@ng-click='launchCreateNewApp(iosString)']").click()
    # +新建APP
    time.sleep(waitSec)
    driver.find_element_by_xpath("//*[@class='checkboxstyle']").click()
    # 选择平台 iOS
    driver.find_element_by_xpath("//*[@ng-model='createAppDetails.name.value']").send_keys(appChineseName)
    #添加名称
    driver.find_element_by_xpath("//*[@value='string:zh-Hans']").click()

    # 找到所有选择项，选择简体中文
    name = "string:%s" %(bundleID)
    print("//*[@value='%s']" %(name))
    # 暂时先用chenzuo - com.chenzuo.cz
    name = "string:com.chenzuo.cz"
    driver.find_element_by_xpath("//*[@value='%s']" %(name)).click()
    driver.find_element_by_xpath("//*[@ng-model='createAppDetails.vendorId.value']").send_keys(bundleID)
    # 找到对应的
    driver.find_element_by_xpath("//*[@ng-click='saveApp()']").click()
    time.sleep(waitSec*1.5)

if __name__ == '__main__':
    print(bundleID)

    login()
    openCIP()

    creatAppId() #生成appid
    addDevices()  # 根据txt地址添加UDID

    ceartCeetificates(0)#生成开发证书
    ceartCeetificates(2)#生成发布证书

    # ceartCeetificates(1)  # 生成开发推送证书
    ceartCeetificates(3)  # 生成发布推送证书

    addProfiles(0) #生成开发配置文件
    addProfiles(2) #生成生产配置文件
    addProfiles(4) #生成Hoc配置文件
    # openiTunesConnect()
    # addNewApp()











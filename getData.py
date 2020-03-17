# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:18:58 2018

@author: Lenovo
"""

# -*- coding: utf-8 -*-

import requests
import urllib
import random
from datetime import datetime

# python2 和 python3的兼容代码
try:
    # python2 中
    import cookielib

    print("user cookielib in python2.")
except:
    # python3 中
    import http.cookiejar as cookielib

    print("user cookielib in python3.")

# session代表某一次连接
huihuSession = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
huihuSession.cookies = cookielib.LWPCookieJar(filename="huihuCookies.txt")

userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
header = {
    # "origin": "https://passport.huihu.cn",
    "Referer": "http://hh.haiper.com.cn/w/wander/user/login/",
    'User-Agent': userAgent,
}


def huihuLogin(account, password):
    #
    print ("开始模拟登录嘻嘻嘻")

    postUrl = "http://hh.haiper.com.cn/w/wander/user/login/"
    postData = {
        "username": account,
        "password": password,
    }

    # 使用session直接post请求
    responseRes = huihuSession.post(postUrl, data=postData, headers=header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    # print(f"text = {responseRes.text}")
    huihuSession.cookies.save()


def isLoginStatus():
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态
    for i in range(2131, 2134):
        routeUrl = "http://hh.haiper.com.cn/w/bench/extend/health/trade/all?nickname=&type=&gender=&level=&range%5Bstart%5D=2014-11-11+14%3A57&range%5Bend%5D=2018-06-06+14%3A57&page=" + str(
            i)

        # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
        try:
            responseRes = huihuSession.get(routeUrl, headers=header, allow_redirects=False)
            result = responseRes.text
        except:
            continue
        start = result.find('<div class="form-control-static form-control-static-list">')
        result = result[start:]
        # print (result)
        for j in range(1, 16):
            start = result.find('擦擦擦图片')
            if start == -1:
                break
            else:
                result = result[start:]
                start = result.find('src="')
                result = result[start + 5:]
                end = result.find('" class="img-rounded"')
                imgpath = result[:end]
                print (imgpath)
                if imgpath == '/attachment/':
                    continue
                randomname = datetime.now().strftime("%Y%m%d_%H%M%S") + str(random.randint(1, 100)) + '.jpg'
                try:
                    urllib.request.urlretrieve(imgpath, './擦擦擦/' + randomname)
                except:
                    continue
        print (i)
    print(f"isLoginStatus = {responseRes.status_code}")
    # print(f"text = {responseRes.text}")
    if responseRes.status_code != 200:
        return False
    else:
        return True


if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    huihuLogin("xxxx", "xxxx")
    isLogin1 = isLoginStatus()
    print(f"is login huihu = {isLogin1}")
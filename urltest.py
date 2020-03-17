# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse


url = "http://www.baidu.com"

# 这种方法 user-agent:python-urllib/3.6 会告诉网站 是python爬虫
# response = urllib.request.urlopen(url)
# print(response.read().decode())

# 需要想办法反扒
# 百度关键字：UA大全，模拟各种浏览器

# 构建请求头信息（反扒第一步）：伪装自己的UA，让服务端认为你是浏览器上网

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",

}
# urllib.request.Request()
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())

print("123")

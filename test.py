import urllib.request

# urllib.request.Request()
url = 'http://www.baidu.com/'
res = urllib.request.urlopen(url=url)
page_source = res.read().decode('utf-8')
print(page_source)


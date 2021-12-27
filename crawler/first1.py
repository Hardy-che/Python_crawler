"""
urllib库（python内置库）
1. urlopen函数
    from urllib import request
    resp = request.urlopen('网址')
    print(resp.read())
    urlopen表示创建了一个url的类文件对象，然后像本地文件一样操作。
    返回值：返回值是一个http.client.HTTPResponse对象，有read(size), readlines以及getcode等方法。
2. urlretrieve将网页下载到本地
"""
from urllib import request
# urlopen
resp = request.urlopen('https://www.baidu.com/')

print(resp.read())

# urlretrieve

request.urlretrieve('http://baidu.com/', 'baidu.html')
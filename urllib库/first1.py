"""
urllib库（python内置库）
1. urlopen函数
    from urllib import request
    resp = request.urlopen('网址')
    print(resp.read())
    urlopen表示创建了一个url的类文件对象，然后像本地文件一样操作。
    返回值：返回值是一个http.client.HTTPResponse对象，有read(size), readlines以及getcode等方法。
2. urlretrieve将网页下载到本地
    request.urlretrieve('网址', '文件名')
3. urlencode函数
    将字典数据转换成URL编码的数据
4. parse_qs函数
    将URL编码数据进行解码
5. urlparse and urlsplit
    拿到一个url，想要对这个url中的各个组成部分进行分割
    两种函数基本一摸一样，urlparse里有params属性， 而urlsplit没有这个params属性
"""
from urllib import request, parse
# urlopen -------------------------------------------------------
resp = request.urlopen('https://www.baidu.com/')

# print(resp.read())

# urlretrieve --------------------------------------------------------
request.urlretrieve('http://baidu.com/', 'baidu.html')

# urlencode ----------------------------------------------------------
data = {'name': '老王', 'age': '18', 'say': 'lol'}

qs = parse.urlencode(data)
print(qs)
print(parse.parse_qs(qs))

# urlparse and urlsplit
url = 'https://edu.csdn.net/learn/24756/280657'

result = parse.urlparse(url)

print(result)
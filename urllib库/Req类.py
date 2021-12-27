"""
request.Request类：如果想要在请求的时候加一些请求头，那么就必须使用request.Request类来实现
比如加一个User-Agent
"""
from urllib import request

header ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36}'
}

rq = request.Request('https://edu.csdn.net/learn/24756/280658', headers=header)

resp = request.urlopen(rq)
print(resp.read())
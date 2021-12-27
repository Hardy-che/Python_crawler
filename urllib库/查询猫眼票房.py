from urllib import request

url = 'https://piaofang.maoyan.com/dashboard'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/96.0.4664.110 Safari/537.36'
}

rq = request.Request(url, headers=header)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))

"""
1. 请求头
2. 响应获取
3. URL
"""
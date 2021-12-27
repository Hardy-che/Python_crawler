from urllib import request

url = 'https://m.biedoul.com/'

resp = request.urlopen(url)
print(resp.read().decode('utf-8'))
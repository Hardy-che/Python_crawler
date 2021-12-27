"""
Http 协议： HyperText Transfer Protocol
HTML: HyperText Markup Language
Https 协议: 是HTTP协议的加密版本， 在HTTP下加入了SSL层， 服务器端口号是443端口
一 URL: Uniform Resource Locator
scheme://host:port/path/?query-string=xxx#anchor
    1. scheme: 访问协议类型 http/https/ftp
    2. host: 主机名， 域名
    3. port: 端口号
    4. path: 查找路径
    5. query-string: 查询字符串
    6: anchor: 锚点（做定位）

二 常见的请求Method
HTTP协议中，定义了八种请求方法
    1. get: 请求数据并不队服务器资源产生影响
    2. post: 向服务器发送数据

三 常见的请求头参数
向服务器发送请求，数据分为三部分，第一个URL 第二个body（post请求中） 第三个（head中）
    1. User-Agent：浏览器名称， 可以通过这个判断是浏览器还是爬虫。
    2. Referer：表明该请求是从哪个URL过来
    3. Cookie: 标识请求发送两次时是否是同一人发送

四 常见的响应状态码
    1. 200：请求正常，正常返回数据
    2. 301：永久重定向。
    3. 302：临时重定向。比如在访问一个需要登录的页面时候。
    4. 400：请求的url在服务器上找不到。（请求错误）
    5. 403：服务器拒绝访问，权限不够。
    6. 500： 服务器内部错误。可能是服务器出现bug 
"""
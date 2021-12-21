import os       # 与操作系统交互的包
import sys      # 与系统相关的参数
import time     # 与时间相关
import math     # 浮点数函数库
import random   # 随机数
import re       # 正则表达式

# OS使用
print(os.getcwd())      # 获取当前工作路径

# SYS使用
print(sys.argv)         # 命令行参数
print(sys.platform)     # 版本
print(sys.path)         # python解释器自动查找所需模块

# time使用
# print(time.time())      # 返回当前时间的时间戳（秒数）
# time.sleep(5)           # 程序暂停5秒
# print(time.localtime())     # 返回跟时间相关所有内容

# math
x = math.cos(math.pi / 2)   # 返回三角函数值

# random
print(random.randrange(1, 20, 7))       # 1~20 步长为7
print(random.randint(1, 100))       # 1~100
x = ["1", "Chehan", "Python", "课程"]
print(random.choice(x))     # 随机取元素
y = range(100)
print(list(y))
z = list(y)
random.shuffle(z)       # 重新排序--操作对象是个list
print(z)
k = random.sample(x, 2)     # 随机拿两个元素 一定小于元素总数
print(z)

# re（正则表达式）
p = "今天中华人民共和国成立了，但是我们都还是老百姓"
print(re.search("，", p))        # 在字符串中寻找
print(re.match("今天", p))        # 字符串开始位置匹配
print(re.split("，", p))         # 字符串的分割
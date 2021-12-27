# map 函数  得到分别元素操作后的结果
def fun(x):
    return x*x


y = [4, 5, 6, 7, 8, 1, 0, 3]
z = list(map(fun, y))
print(z)

# reduce 函数  找最大值
from functools import reduce


def fun(k, h):
    m = k if k > h else h
    return m


nuu = [4, 5, 16, 55, 67, 90, 3]
max_find = reduce(fun, nuu)
print(max_find)

# 迭代器
x1 = ["韩彻",  "曲倞萱", "hardy"]

y1 = iter(x1)
print(next(y1))
print(next(y1))


# 生成器
def gen(n):
    for i in range(n):
        yield i*i


x = gen(5)
for i in x:
    print(i, end=" ")
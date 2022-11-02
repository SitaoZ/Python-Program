# syntax
# max(iterable, /, *, key=None)
# max(iterable, /, *, default, key=None)
# max(arg1, arg2, /, *args, key=None)

# 方式1 可迭代对象
a = [1,2,3]
print(max(a))

b = (1,2,3,4)
print(max(b))

c = {'A':1, 'B':10, 'C':2, 'D':5}
print(max(c))

# 方式2 key指定
print('最大值的key:',max(c, key=c.get))
print('最大值:',max(c.values()))


# 给定参数
print(max(1,3,4))


## Python-Program
The repository contains my scripts in bioinformatics.
All the scripts are executed in python3

### 1. python trick 
#### 1.1 成员判断
```python
# 成员判断使用集合(set)和字典(dict)速度较快O(1), 使用列表(list)和元组(tuple)慢O(n)
a = set([1,2,3]) # 集合
1 i in a
b = {'A':1, 'B':2} # 字典
'A' in b 
```
#### 1.2 字符串拼接
```python
# O(n) join > O(n**2): + +=
seq = ['A', 'T', 'C', 'G']
''.join(seq)
```

#### 1.3 迭代加速

```python
# 许多工具都有两种实现方式，一种是列表形式(list form)，一种是迭代器形式(iterator form)
range() xrange()
map itertools.map
list comprehensions generator expressions
dict.items dict.iteritems()
# 一般情况下，迭代器的形式比列表的形式快
```

#### 1.4 C模块加速
list, tuple, set, dict都有相应的C优化的模块 numpy中的array, itertools, collections.deque 

#### 1.5 内建函数
内建函数比自己创建的函数执行快
```python
# map（function_to_apply, list_of_inputs
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x : x<0, number_list))

# reduce
from functools import reduce
product = reduce(lambda x, y: x*y, [1,2,3,4])

```

#### 1.6 三元操作符

```python
# value_if_true if condition else value_if_false
v = 19 
value = "greate_than_zero" if v > 0 else "less_than_zero"
```
### 2. python one-liner
```python
python -c "print unichr(234)"
# split file
python -c "import sys;[sys.stdout.write(' '.join(line.split(' ')[2:])) for line in sys.stdin]" < input.txt
# csv to json
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```

[one-liner](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)

### 3. jupyter 

```bash
$ # 远程登陆服务器jupyter
$ jupyter notebook --no-browser --port=8888 # 远程服务器上启动
$ http://serverIP:8888/ # 客户端启动，即可编辑
$ # 更改notebook目录
$ vi .jupyter/jupyter_notebook_config.py # c.NotebookApp.notebook_dir = "xxx"
```

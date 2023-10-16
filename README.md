## Python-Program
The repository contains my scripts in bioinformatics.
All the scripts are executed in python3

### 1. python speed 
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
```

### 2. jupyter 

```bash
$ # 远程登陆服务器jupyter
$ jupyter notebook --no-browser --port=8888 # 远程服务器上启动
$ http://serverIP:8888/ # 客户端启动，即可编辑
$ # 更改notebook目录
$ vi .jupyter/jupyter_notebook_config.py # c.NotebookApp.notebook_dir = "xxx"
```

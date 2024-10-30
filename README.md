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

```python
# max/min
max(stats, key=stats.get) # 返回字典中值最大对应的键
min(stats, key=stats.get) # 返回字典中值最小对应的键

# sorted
list_to_be_sorted = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
newlist = sorted(list_to_be_sorted, key=lambda d: d['name']) # 根据字典值排序
from operator import itemgetter
newlist = sorted(list_to_be_sorted, key=itemgetter('name'))

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
- 远程登录
```bash
$ # 远程登陆服务器jupyter
$ jupyter notebook --no-browser --port=8888 # 远程服务器上启动
$ http://serverIP:8888/ # 客户端启动，即可编辑
$ # 更改notebook目录
$ vi .jupyter/jupyter_notebook_config.py # c.NotebookApp.notebook_dir = "xxx"
```

- 代码转换
```bash
$ # ipynb to py script
$ jupyter nbconvert --to script plot_PCA.ipynb
```

- jupyter lab [新一代jupyter](https://jupyter.org/install)    
- step1 生成密码   
```python
>>> from jupyter_server.auth import passwd
>>> passwd()
# Enter password: 
# Verify password:
```
- step2 生成配置文件   
```bash 
$ jupyter lab --generate-config # 生成配置文件
```
- step3 修改配置文件   
```bash
$ grep -v "^#" .jupyter/jupyter_lab_config.py | sed '/^$/d'
c = get_config()  #noqa
c.ExtensionApp.open_browser = False
c.LabServerApp.open_browser = False
c.LabApp.open_browser = False
c.ServerApp.allow_remote_access = True
c.ServerApp.ip = 'xxx.xxx.xxx.xxx'
c.ServerApp.notebook_dir = '/data/zhusitao/project/'
c.ServerApp.open_browser = False
c.ServerApp.password = 'xxxxxxxxxxxx'
c.ServerApp.password_required = True
c.ServerApp.port = 8888

```
- step4 命令行启动   
```bash
$ jupyter lab --no-browser --port=8888
```

- step5 客户端web打开   
http://xxx.xxx.xxx.xxx:8888/lab
### 4. python conding style
良好的编码风格产生优质代码，让代码更加具有活力。自己都看不下去的代码，不要指望别人会看，大概率进垃圾箱。
[PEP 8](https://peps.python.org/pep-0008/)
#### 4.1 代码布局 Code Lay-out
1. 每个缩进级别使用四个空格，不要使用tab。
延续行应该使用Python隐式的圆括号、方括号和大括号内的行连接垂直对齐换行元素，或者使用悬挂缩进。当使用悬挂缩进时，
应考虑以下几点:第一行不应该有参数，并且应该使用进一步的缩进来清楚地将其区分为延续行。
2. 每行最长不超过79字符
换行的首选方法是在括号、方括号和大括号内使用Python隐含的行延续。通过将表达式括在括号中，可以将长行分隔成多行。这些应该优先于使用反斜杠进行行延续。
3. 二元操作符换行
```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```
4. 空白行的使用
在类，函数，和逻辑块之间使用空白行，增强代码的可读性。
5. 导入模块应该在单独的行上分别导入
```python
import os
import sys
```
#### 4.2 引号
字符串中，单引号和双引号是相同的，但是如果字符串中出现单引号或者双引号，应该选择另一个字符以免出现反斜杠。
#### 4.3 表达式和语句中的空白
#### 4.4 关键代码处记得写注释
- 函数注释
给函数的参数和返回值填写注释，可以使用默认值。注释储存在函数对象的__annotations__文件中。
```python
def func(a:str , b:int , c:float) ->str:
    return a+str(b+c)
func.__annotations__ # 获取注释对象，以字典的形式返回
```
#### 4.5 命名规范
- 类名首字母大写
- 函数名应该是小写的，必要时用下划线分隔，以提高可读性
#### 4.6 函数return的一致性，if else都要有相应的返回值。

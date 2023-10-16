## Python-Program
The repository contains my scripts in bioinformatics.
All the scripts are executed in python3

### python speed 

```python
# python 加速技巧
# 成员判断使用集合和字典速度较快O(1), 使用列表和元组慢O(n)
a = set([1,2,3])
1 i in a


```

### jupyter 

```bash
$ # 远程登陆服务器jupyter
$ jupyter notebook --no-browser --port=8888 # 远程服务器上启动
$ http://serverIP:8888/ # 客户端启动，即可编辑
$ # 更改notebook目录
$ vi .jupyter/jupyter_notebook_config.py # c.NotebookApp.notebook_dir = "xxx"
```

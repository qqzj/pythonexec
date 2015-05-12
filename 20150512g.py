# coding=utf-8
# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中
import sys
print sys.path
print
sys.path.append('C:/Windows/System32')
print sys.path
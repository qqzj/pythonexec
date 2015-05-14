# -*- coding: utf-8 -*-
# 
# 系统调用
import os
name = os.name
if name=='nt':
    print name
else:
    print os.uname()
print os.path.abspath('.')


# 文件操作
f = open('C:/Python27/LICENSE.txt', 'r')
# print f.read()
f.close()

# 代码更佳简洁，并且不必调用f.close()方法
with open('C:/Python27/LICENSE.txt', 'r') as f:
    # print f.read()
    pass

dirs = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.pyc']
print dirs

print

files = [y for y in os.listdir('.') if os.path.isdir(y)]
print files

print
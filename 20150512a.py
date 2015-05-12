# -*- coding: utf-8 -*-
# 匿名函数

def a():
    return lambda x:x*x;
b = a()
print b
print b(2)

a = lambda x,y:x*y
print a
print a(3, 2)

# -*- coding: utf-8 -*-
# 【必选参数】
# 一定要有，否则报错
# 
# 【默认参数】=
# 必选参数在前，默认参数在后
# 
# 【可变参数】*
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
# 
# 【关键字参数】**
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到
# 
# 【参数组合】
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
# def func(a, b, c=0, *args, **kw):
# 
# 【神奇】
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# 
print abs(-12)
print abs(12)
print int(123)
print int(123.45)
print float(123.45)
print str(123.45)
print unicode(123.45)
print bool(123.45)
print bool(0)
a = int
print a(1234.56789)
def area_of_circle(r, PI=3.14):
    return PI*r*r
print area_of_circle(2)
print area_of_circle(2, 3)

def add_end(a=[]):
    a.append('END')
    return a
print add_end([1,2,3,4])
print add_end()
print add_end()
print add_end()
print add_end()

def calc(*numbers):
    print numbers
calc(1,2,3,4,5,6)
calc()
nums = [3,4,45,5,6,7,8,9]
calc(*nums)

def person(name,age,*args,**kw):
    print name,
    print age,
    print args,
    print kw
person('wangchaojie', 25)
args = ['VeryGood', 'FuckMe']
kw = {'city':'Beijing','sex':'male'}
person('wangchaojie', 25, *args,**kw)
person('wangchaojie', 25, *args,**{'city':'Beijing','sex':'male'})

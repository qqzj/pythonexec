# -*- coding: utf-8 -*-
# 动态语言和静态语言最大的不同，
# 就是函数和类的定义，
# 不是编译时定义的，
# 而是运行时动态创建的
# 
def say(self):
    print 'I\'m a pretty boy.'
hi = type('hello', (object,), dict(speak=say))
h = hi()
h.speak()
print type(hi)
print type(h)
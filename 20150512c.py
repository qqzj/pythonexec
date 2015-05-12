# coding=utf-8
# -*- coding: utf-8 -*-
# 简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调
# 用这个新函数会更简单
import functools
# int第二个参数base代表当前传入的第一个参数的进制，
# 并非要转换的进制，
# 没有转换功能
print int('123')
print int('16', 10)
print int('00FFCC', 16)

int2 = functools.partial(int,base=2)
int16 = functools.partial(int,base=16)
print int2('1000')
print int16('1000')

print max(1,2,3)
max10 = functools.partial(max,10)
print max10(1,2,3)
#-*- coding=utf-8 -*-
a = [x for x in range(1, 10)]
print sum(a)
def lazy_sum():
    def my_sum(x):
        return sum(x)
    return my_sum
b = lazy_sum()
print b
print b(a)
print lazy_sum()
print lazy_sum()
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
print lazy_sum()
print lazy_sum() == lazy_sum()
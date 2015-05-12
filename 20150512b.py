# coding=utf-8
# 现在，
# 假设我们要增强test()函数的功能，
# 比如，在函数调用前后自动打印日志，
# 但又不希望修改test()函数的定义，
# 这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print '调用%s()'%(func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def test(x):
    return '%d%s'%(x,'2015-5-12 11:40:21')

print test(1)

print '======================'

a = log(test)
print a(1)
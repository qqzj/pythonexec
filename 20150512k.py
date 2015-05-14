# coding=utf-8
from types import MethodType
class student(object):
    # 使用__slots__要注意，
    # __slots__定义的属性仅对当前类起作用，
    # 对继承的子类是不起作用的
    # 除非在子类中也定义__slots__，
    # 这样，
    # 子类允许定义的属性就是自身的__slots__加上父类的__slots__
    __slots__=('name', 'get_sex')
    pass
stu = student()
stu.name = 'Jack'
print stu.name

def get_sex(self):
    return 'Female'

stu.get_sex = MethodType(get_sex, stu, student)

print stu.get_sex()
#-*- coding: utf-8 -*-
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
# 直接用属性比较直观，调用方法不直观
class stu(object):
    @property
    def foo(self):
        print 'A'
    @foo.setter
    def foo(self, x):
        print 'B'
    @foo.getter
    def foo(self):
        print 'C'
    @property
    def age(self):
        print 'D'
    @age.getter
    def age(self):
        print 'E'
    @age.setter
    def age(self, x):
        print 'F'
s = stu()
s.foo = 100
s.foo
s.age = 100
s.age
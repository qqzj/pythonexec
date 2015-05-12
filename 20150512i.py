# coding=utf-8
# 
# (object)，表示该类是从哪个类继承下来的，
# 继承的概念我们后面再讲，
# 通常，
# 如果没有合适的继承类，
# 就使用object类，
# 这是所有类最终都会继承的类。
# 
class student(object):
    # 注意到__init__方法的第一个参数永远是self，
    # 表示创建的实例本身
    # 但self不需要传，
    # Python解释器自己会把实例变量传进去
    # 
    # 有些时候，
    # 你会看到以一个下划线开头的实例变量名，
    # 比如_name，
    # 这样的实例变量外部是可以访问的，
    # 但是，按照约定俗成的规定，
    # 当你看到这样的变量时，
    # 意思就是，“虽然我可以被访问，
    # 但是，请把我视为私有变量，
    # 不要随意访问”。
    # 
    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex
    def print_score(self):
        print '%s:%s'%(self.name, self.score)
    def getSex(self):
        return self.__sex

bart = student('Jack', '90', 'female')
bart.print_score()
print bart.name
print bart.getSex()

print bart
print int('0x000000000268CCF8', 16)

print isinstance(bart, student)
print type(bart)
import types
if(type('123') == types.StringType):
    print 'OK'
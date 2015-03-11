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

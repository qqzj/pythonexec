classmates = ['apple', 'ibm', 'dell', 'lenovo', 'Honor', 'Assend', 'Sumsung']
print len(classmates)
for x in xrange(0,len(classmates)):
    print classmates[x],

print

for x in classmates:
    print x,

print

from collections import Iterable
print isinstance(123, Iterable)
print isinstance(classmates, Iterable)

print 

for x,y in enumerate(classmates):
    print x,y

for x,y in ((1,1),(2,4),(3,9)):
    print x,y

for x in ((1,1),(2,4),(3,9)):
    print x

print xrange(0,10)
print range(0,10)
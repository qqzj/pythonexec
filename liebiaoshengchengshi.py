print range(1, 10)
L = []
for x in xrange(1, 11):
    L.append(x*x)
print L

print [x*x for x in xrange(1, 11)]

print [a+b for a in xrange(1, 11) for b in xrange(10, 21)]

print

print ['%d*%d=%d'%(a, b, a*b) for a in xrange(1, 10) for b in xrange(1, 10)]

print

import os
print [d for d in os.listdir('.')]

from collections import Iterable

print
di = 123;
if(isinstance(di, Iterable)):
    for x,y in di.iteritems():
        print x,y
else:
    print 'variable [di] can\'t be Iterable'

print
di = {'Dell':85, 'Lenovo':92, 'Apple':94, 'IBM':89}
print [a+'=>'+str(b) for a,b in di.iteritems()]

print [x for x in xrange(1, 10)]
print (x for x in xrange(1, 10))

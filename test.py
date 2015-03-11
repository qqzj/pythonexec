import sys
import hashlib
for a in xrange(1,10):
    for b in xrange(1,a+1):
        print '%d*%d=%d'%(a, b, a*b),
    print
print sys.platform
print hashlib.md5('admin').hexdigest()
a = raw_input('Please enter your name:')
print
print 'Hello, %s'%(a),
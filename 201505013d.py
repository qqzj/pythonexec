# -*- coding: utf-8 -*-
import os
print 'hello'
if os.name!='nt':
    pid = os.fork()
    if pid==0:
        print 'a'
    else:
        print 'b'
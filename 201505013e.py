# -*- coding: utf-8 -*-
import time, threading
print dir(time)
print type(time.__name__)
print type(time.sleep)
print time.clock()
print time.time()
print time.localtime()
print time.localtime()
count = 65
for x in range(26):
    time.sleep(0.1)
    print chr(count),
    count = count + 1
print
count = 97
for x in range(26):
    time.sleep(0.1)
    print chr(count),
    count = count + 1

li = ['apple', 'orange', 'pinapple', 'watermelon']
tu = ('apple', 'orange', 'pinapple', 'watermelon')
di = {'china':'apple', 'english':'orange', 'malay':'pinapple', 'mexco':'watermelon'}
se = [('apple', 'orange', 'pinapple', 'watermelon')]

print li
print tu
print di
print se

print li[0]
print tu[1]
print di['malay']
print li[3]

ran = range(100)
print ran[::2]


import os
from collections import Iterable
dirlist = os.listdir('.')
if(isinstance(dirlist, Iterable)):
    for d in dirlist:
        print d,

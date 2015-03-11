classmates = ('apple', 'ibm', 'dell', 'lenovo')
t = (1,)
print classmates
print t
classmates = ('apple', 'ibm', 'dell', [], 'lenovo')
print classmates
classmates[3].append('A')
classmates[3].append('B')
classmates[3].append('C')
classmates[3][1] = 'X'
print classmates
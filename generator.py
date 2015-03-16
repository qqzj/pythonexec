gen =  (x for x in xrange(1, 1000000, 3))
print gen.next(),
print gen.next(),
print gen.next(),
print gen.next(),
print gen.next(),
print gen.next(),
print gen.next(),
print gen.next(),

print

def fab(num):
    li = [0,1]
    while li[-1]+li[-2] <= num:
        li.append(li[-1]+li[-2])
    yield li
a = fab(5000)
print a
print a.next()

def generator_func():
    print 'Step 1:'
    yield 1
    print 'Step 2:'
    yield 4
    print 'Step 3:'
    yield 9

b = generator_func()
print b
for x in b:
    print x

print range(0, 10)
a = xrange(0, 10)
print a
def m(x):
    return x*x
a = [x for x in range(1, 10)]
print map(m, a)

b = [x for x in range(1, 101)]
def r(x, y):
    return x+y

def rr(x, y):
    return x*10+y

print reduce(r, b)
print reduce(rr, a)

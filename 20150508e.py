def is_odd(x):
    return x % 2 == 0
a = [x for x in range(1,10)]
print filter(is_odd, a)
def strFormat(str):
    str = str.lower();
    return str[0].upper()+str[1:].lower()
a = ['adam', 'LISA', 'barT']
print map(strFormat, a)

def prod(x,y):
    return x*y
b = [x for x in range(1, 6)]
print reduce(prod, b)
def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)
print fact(5)
print fact(10)

def fab(num):
    li = [0,1]
    while li[-1]+li[-2] <= num:
        li.append(li[-1]+li[-2])
    return li
print fab(5000)
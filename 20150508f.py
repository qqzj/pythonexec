print sorted([36, 5, 12, 9, 21])

def reserved_cmp(x,y):
    if(x>y):
        return -1
    if(x<y):
        return 1
    if(x==y):
        return 0
print sorted([36, 5, 12, 9, 21], reserved_cmp)
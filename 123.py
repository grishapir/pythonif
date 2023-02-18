rat = [10, 12, 14,]
def foo(a):
    c = 0
    for i in range(len(a)):
        c += a[i]
    print(c)     
foo(rat)


rat = [10, 12, 14,]
def foo(a):
    c = 1
    for i in range(len(a)):
        c *= a[i]
    print(c)     
foo(rat)
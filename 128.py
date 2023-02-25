cpi = [1, 2, 3, 4, 4, 4, 3, 2, 5]
def foo(a):
    c = []
    
    for i in range(len(a)):
        flag = True
        for j in range(len(a)):
            if a[i] == a[j] and  i != j:
                flag = False
        if flag == True:
            c.append(a[i])
    print(c)
foo(cpi)
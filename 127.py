a = "Это должно быть"
c = 0
def foo(a, c):
    for i in range(len(a)):
        if a[i] != " ":
            c+=1
            print(c)
foo(a, c)
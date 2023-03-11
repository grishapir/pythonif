n = int(input("дите степень двойки"))
l = 2
def a(n, l):
    if n == l:
        return "yes"
    elif n>l:
        return a(n, l*2)
a(n, l)
print(a(n, l))

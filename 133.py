m = 0
n = 1
def a(m, n):
    if m == 0:
        return n+1
    if m>0 and n == 0:
        return a(m-1, 1)
    if m>0 and n>0:
        return a(m-1,a(m,n-1))
a(m, n)
print(a(m,n))
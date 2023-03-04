n = int(input("ведите число"))
def fact(n, max ):
    if n != max:
        print(n)
        fact(n+1, max)
fact(1,n+1)
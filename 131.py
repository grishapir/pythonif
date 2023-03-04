a = (int(input("Введите число")))
b = (int(input("Введите число")))
def fact(a, b):
    if a < b:
        print(a)
        fact(a+1, b)
    if a>b:
        print(a)
        fact(a-1, b)
fact(a, b)
        



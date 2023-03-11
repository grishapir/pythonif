n = 13
x=0
def a(n):
    x = 0
    if n != 0:
        x+= n%10
        return x+a(int(n/10)) 
    else: 
        return x   

print(a(n))
import random
print(random.sample(range(99, 1000), 222))
parol = input("Введите два числа\n")
def MyFunc(parol):
    for num in ['1','2','3','4','5',"6","7","8","9"]:
        for elem in str(parol):
            if num == elem:
                print("Неконкретный два числа")
parol = input ("Введите два числа\n")
MyFunc(parol)
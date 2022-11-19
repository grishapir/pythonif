parol = input("Введите пароль\n")
def MyFunc(parol):
    for num in ['!','+','-','*','_']:
        for elem in str(parol):
            if num == elem:
                print("Неконкретный пароль")
parol = input ("Введите пароль\n")
MyFunc(parol)
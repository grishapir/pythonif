log={}
pas={}
o=input("Введите команду выход или регистрация")

if o == "регистрация":
    a = input("Введите логин")
    while log == a:
        print("невозможно")
        a = input("Введите логин")
    log["логин"] = a
    b = input("Введите пароль")
    c = input("Введите потверждения пароля")
    while b != c:
        print("Так невозможно")
        b = input("Введите пароль")
        c = input("Введите потверждения пароля")
    
    while pas == b:
        print("Так невозможно")
        b = input("Введите пароль")
        c = input("Введите потверждения пароля")
    pas["пароль"] = b
    for key in log:
        print(key,":", log[key])
    for key in pas:
        print(key,":", pas[key])
        
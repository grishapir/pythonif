a=input('Введите парол\n')
b=input('Введите логин\n')
while a != '5960' and b != 'login':
    a=input("ПАРОЛЬ НЕ СОВПАДАЕТ\n")
    b=input('логин не совподает')
    print("не все совпадает")
else:
  print('Все совподает')
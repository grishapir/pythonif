comand=input('Введите команду').lower()
while comand!='не играю' and comand!='у меня шиза':
    if comand == "танкист":
        print('У тебя шиза? какая стата')
        slovo = input("Введите стату:")
        print("стата:"+slovo)
        print('Вызывайте дурку')
    elif comand == "бравлер":
        print('Лучше бы ты не играл')
        print('И то лучше чем Танкист')
    
    comand = input('Введите команду')
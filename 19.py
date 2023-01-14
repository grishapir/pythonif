myList = ['дом',2]
while True:
    a = input('Введите команду: редактирование по имени, добавить по номеру, добавить, удалить, показать по номеру, показать список ')
    while a == 'добавить' and a == 'удалить' and a == 'показать по номеру' and a == 'показать список':
        a = input('Введите команду: редактирование по имени, добавить по номеру, добавить, удалить, показать по номеру, показать список ')
    if a =='добавить':
        myList.append(input('Введите новый элемент списка'))
    if a == 'удалить':
        myList.remove(input('Введите элемент списка'))
    if a == 'показать по номеру':
        for i in range(0,len(myList)):
            print(myList[i])
    if a == 'показать список':
        print(myList)
    if a == 'добавить по номеру':
        p = input('Введите изменнённое слово')
        i = int(input('Введите индекс'))
        myList[i] = p
    if a == 'редактирование по имени':
        searchedValue = input()
        if searchedValue in myList:
            myList[myList.index(searchedValue)] = input('Введите новое значение')
            
products = ['Помыть голову', 'Пойти за хлебом', 'Поиграть в бомжа']
products.remove(input('Удали из  список дело'))
products.append(input('Добавь в список дело'))
products.insert(1, input('Перепишыте дело под номером 1'))
if"Помыть голову" in products:
    products.insert(0, input('Перепишыте дело под номером 0'))
for i in range(0,len(products)):
    print(products[i])
print(products)

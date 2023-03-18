import mylib
import random
# массивы и функция vyvodPolya в файле mylib.py           

        
mylib.vyvodPolya(mylib.vidimost_polya)
game = True
a = random.randint(0, 11)
b = random.randint(0, 11)
s = random.randint(0, 11)
d = random.randint(0, 11)
f = random.randint(0, 11)
g = random.randint(0, 11)
mylib.pole[a][b] = "b"
mylib.pole[f][g] = "b"
mylib.pole[s][d] = "b"
while game:
    if mylib.vidimost_polya[a][b] == "b" or mylib.vidimost_polya[s][d] == "b" or mylib.vidimost_polya[f][g] == "b":
        print("Игра окончена")
        game = False
        break
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    while stroka <0 or stroka >12 or stolb <0 or stolb>12:
        print("Неа")
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
    # передадим не номера строки и столбца, а индексы
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False
def CheckBombs(pole):
    for i in range (len(pole)):
        for j in range(len(pole[i])):
            bombs = 0
            if pole[i][j] != "b":
                if i != 0 and i != 11:
                    if pole[i-1][j]:
                        bombs+=1
                    if pole[i+1][j]:
                        bombs+=1
                elif i== 0
                    if pole[i+1][j]:
                        bombs+=1
                elif i == 12:
                    if pole[i-1][j]:
                        bombs+=1
                if j !=0 and j != 11:
                    
                    if pole[i][j-1]:
                        bombs+=1
                    if pole[i][j+1]:
                        bombs+=1

                
print("Всё поле открыто!")

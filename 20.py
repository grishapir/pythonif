pole = [["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*"]]
a = int(input("Куда ты хочешь поставить о"))
b = int(input("Куда ты хочешь поставить о"))
pole[a][b] = "o"
for stroka in pole:
    for kletka in stroka:
        print(kletka,end ="")
    print()
d = input("Выбери куды пойдешь: направо, налево, вниз, вверх")
if d == "направо":
    pole[a][b] = "*"
    pole[a][b+1] = "o"
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end ="")
        print()
if d == "налево":
    pole[a][b] = "*"
    pole[a][b-1] = "o"
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end ="")
        print()
if d == "вниз":
    pole[a][b] = "*"
    pole[a+1][b] = "o"
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end ="")
        print()
if d == "вверх":
    pole[a][b] = "*"
    pole[a-1][b] = "o"
    for stroka in pole:
         for kletka in stroka:
            print(kletka,end ="")
         print()
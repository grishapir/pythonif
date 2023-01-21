pole = [["-","-","-","-","-","-","-","-"],
        ["*","*","*","*","*","*","*","-"],
        ["-","*","!","*","!","*","*","-"],
        ["-","!","*","*","!","*","*","-"],
        ["-","*","*","*","*","*","*","-"],
        ["-","!","!","*","!","*","*","-"],
        ["-","*","*","*","!","*","*","-"],
        ["-","*","*","*","+","*","*","-"],
        ["-","-","-","-","-","-","-","-"]]
a = 7
b = 4
pole[a][b] = "+"
for stroka in pole:
    for kletka in stroka:
        print(kletka,end =" ")
    print()
while True:
    d = input("куды пойдешь: направо, налево, вверх, вниз")
    while d != "направо" and d != "налево" and d != "вверх" and d != "вниз":
        input("куды пойдешь: направо, налево, вверх, вниз")
    if d == "направо":
        if pole[a][b+1] == "-":
            print("Так не возможнно")
        elif pole[a][b+1] == "!":
            print("и так не возможно")
            a = 7
            b = 4
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
        else:
            pole[a][b] = "*"
            pole[a][b+1] = "+"
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
    if d == "налево":
        if pole[a][b-1] == "-":
            print("Так не возможнно")
        elif pole[a][b-1] == "!":
            print("и так не возможно")
            a = 7
            b = 4
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
        else:
            pole[a][b] = "*"
            pole[a][b-1] = "+"
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
    if d == "вниз":
        if pole[a+1][b] == "-":
            print("Так не возможнно")
        elif pole[a+1][b] == "!":
            print("и так не возможно")
            a = 7
            b = 4
        else:
            pole[a][b] = "*"
            pole[a+1][b] = "+"
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
    if d == "вверх":
        if pole[a-1][b] == "-":
            print("Так не возможнно")
        elif pole[a-1][b] == "!":
            print("и так не возможно")
            a = 7
            b = 4
        else:
            pole[a][b] = "*"
            pole[a-1][b] = "+"
            for stroka in pole:
                for kletka in stroka:
                    print(kletka,end =" ")
                print()
if a == 1 and b == 0:
    print('Ты победил')
    a = 7
    b = 4

class Student:
    def __init__(self, a, b, c, v):
        self.fam = a
        self.inic = b
        self.num = c
        self.yspev = v
spisoc = [Student("Локовоч", "Иван Иванович", 2, 5), Student("Фролов", "Артем Игнатович", 56, 2), Student("Котов", " Максим Иванович", 1, 4)]
for i in spisoc:
    if i.yspev >= 4:
        print(i.inic)
    
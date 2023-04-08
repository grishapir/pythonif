class NPC:
    def __init__(self, n, p, r, hp):
        self.name = n
        self.profesia = p
        self.rost = r
        self.hp = hp
    def privet(self):
        print("Привет меня зовут", self.name)
    def uslugi(self):
        print("Привет купи мои товары", self.profesia)
    def poka(self):
        print("Пока")
        
        
        
        
        
human = NPC("Яков", "Страствующий торговец", 150, 100 )
human2 = NPC("котов", "фермер", 175, 150 )
human3 = NPC("моков", "кузнец", 210, 110 )
human2.privet()
human2.uslugi()
human2.poka()
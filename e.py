class Slime:
    def __init__(self, n, r, v, c):
        self.name = n
        self.razmer = r
        self.ves = v
        self.color = c
    def ispug(self, otherSlime):
        if otherSlime.ves > self.ves:
            return True
        else:
            return False
sli = Slime("первый", "100", 220, "red")
slim = Slime("второй", "500", 1020, "blue")
if sli.ispug(slim):
    print("hgvnhg")
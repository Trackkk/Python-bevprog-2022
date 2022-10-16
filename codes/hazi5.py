class Team:
    def __init__(self, nev, projekt, szerepkor):
        self.nev = nev
        self.projekt = projekt
        self.szerepkor = szerepkor

    def __str__(self):
        return "-- Developer létrehozva. --\n" + self.nev + " a " + \
               self.projekt + "-en dolgozik " + self.szerepkor + " szerepkörben."

    def __eq__(self, uj_dolgozo):
        return self.nev + " és " + uj_dolgozo.nev + " dolgoznak egy projekten."


def check():
    # dolgozok megadása
    dolgozok = [Team("Ricsi", "SolArch", "Frontend"), Team("Angéla", "ZerTeng", "Tesztelő"), Team("Peti", "KefERP", "Backend"), Team("Éva", "KefERP", "Frontend")]
    # teszteles
    for i in range(len(dolgozok)):
        print(dolgozok[i])
    print()
    for i in range(len(dolgozok)):
        for j in range(len(dolgozok)):
            if i != j and j < i and dolgozok[i].projekt == dolgozok[j].projekt:
                print(dolgozok[i] == dolgozok[j])


if __name__ == "__main__":
    check()

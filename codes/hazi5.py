def hazi5():
    class Team:
        def __init__(self, nev, munka, szerepkor):
            self._nev = nev
            self._munka = munka
            self._szerepkor = szerepkor
            # print("-- Developer létrehozva. --")

        def __str__(self):
            return "-- Developer létrehozva. --\n" + \
                   self._nev + " a " + \
                   self._munka + "-en dolgozik " + \
                   self._szerepkor + " szerepkörben."

        def __eq__(self, uj_dolgozo):
            if self._munka == uj_dolgozo._munka:
                return "\n" + self._nev + " és " + uj_dolgozo._nev + " dolgoznak egy projekten."
            return ""

# tesztek
    dolgozok = [Team("Ricsi", "SolArch", "Frontend"), Team("Angéla", "ZerTeng", "Tesztelő"), Team("Peti", "KefERP", "Backend"), Team("Éva", "KefERP", "Frontend")]

    for i in range(len(dolgozok)):
        print(dolgozok[i])

    for i in range(len(dolgozok)):
        for j in range(len(dolgozok)):
            if i != j and j < i:
                print(dolgozok[i] == dolgozok[j])


hazi5()

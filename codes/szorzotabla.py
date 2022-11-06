def szorzotabla():
    elrendezes = "{0:>4}{1:>1}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}{13:>5}"
    print(elrendezes.format("", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))

    print("\t:------------------------------------------------------------", sep="")

    lista = []
    for i in range(0, 12):
        for j in range(1, 13):
            lista.append(j * (i + 1))
        print(elrendezes.format(str(i + 1), ":", lista[0], lista[1], lista[2], lista[3], lista[4], lista[5],
              lista[6], lista[7], lista[8], lista[9], lista[10], lista[11]))
        lista = []


if __name__ == "__main__":
    szorzotabla()

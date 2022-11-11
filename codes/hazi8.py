def hazi8():
    with open('hazi.txt', 'r', encoding='utf-8') as be:
        tartalom = be.readlines()
        szurtlista = []
        for i in range(len(tartalom)):
            szurtlista.append("")

        import string
        for i in range(0, len(tartalom)):
            for j in tartalom[i]:
                if j not in string.punctuation and j != "\n":
                    szurtlista[i] = szurtlista[i] + j

        uj_lista = []
        for i in szurtlista:
            if not i.__eq__(""):
                uj_lista.append(i)

        kis_mh = ['á', 'a', 'é', 'e', 'í', 'i', 'ó', 'ő', 'ö', 'o', 'ú', 'ű', 'ü', 'u']
        nagy_mh = ['Á', 'A', 'É', 'E', 'Í', 'I', 'Ó', 'Ő', 'Ö', 'O', 'Ú', 'Ű', 'Ü', 'U']

        mh_nelkul = []
        for i in range(len(uj_lista)):
            mh_nelkul.append("")

        for i in range(0, len(uj_lista)):
            for j in uj_lista[i]:
                if j not in kis_mh and j not in nagy_mh:
                    mh_nelkul[i] = mh_nelkul[i] + j

        minden_mentes = []
        for i in range(len(mh_nelkul)):
            minden_mentes.append("")

        for i in range(len(mh_nelkul)):
            for j in mh_nelkul[i]:
                if j != " ":
                    minden_mentes[i] = minden_mentes[i] + j

    with open('kimenet.txt', 'w', encoding='utf-8') as ki:
        for i in range(0, len(minden_mentes)):
            if (i+1) % 3 == 0:
                ki.write(minden_mentes[i] + "\n")


if __name__ == "__main__":
    hazi8()

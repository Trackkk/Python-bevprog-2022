def main():
    bekert = str(input("Adj meg egy szót: "))
    palindrom = 1
    duplabetuvolt = 0
    irasjelek = "!\"#$%&'()*+,-./:;<=>?@[\\]^ _˘`{|}~"

    irasjel_nelkuli = ""
    for i in bekert.lower():
        if i not in irasjelek:
            irasjel_nelkuli += i

    szo0 = irasjel_nelkuli.replace('á', 'a')
    szo1 = szo0.replace('á', 'a')
    szo2 = szo1.replace('é', 'e')
    szo3 = szo2.replace('í', 'i')
    szo4 = szo3.replace('ó', 'o')
    szo5 = szo4.replace('ö', 'o')
    szo6 = szo5.replace('ő', 'o')
    szo7 = szo6.replace('ú', 'u')
    szo8 = szo7.replace('ü', 'u')
    szo9 = szo8.replace('ű', 'u')
    szo = szo9

    for i in range(len(szo)):

        if i == int(len(szo) / 2):
            break
        else:
            if duplabetuvolt > 0:
                duplabetuvolt -= 1
                continue

            if szo[i] == 'n' or szo[i] == 's' or szo[i] == 'z' or szo[i] == 't' or szo[i] == 'c' or szo[i] == 'd' or \
                    szo[i] == 'g' or szo[i] == 'l':

                if szo[i] == 'd' and szo[i + 1] == 'd' and szo[i + 2] == 'z' and szo[i + 3] == 's':
                    duplabetuvolt = 3
                    if szo[i] != szo[-i - 4] or szo[i + 1] != szo[-i - 3] or szo[i + 2] != szo[-i - 2] or szo[i + 3] != \
                            szo[-i - 1]:
                        palindrom = 0

                elif szo[i] == szo[i + 1]:
                    if (szo[i] == 'd' and szo[i + 1] == 'd' and szo[i + 2] == 'z' and szo[i + 3] != 's') or (
                            szo[i] == 'n' and szo[i + 2] == 'y') or (szo[i] == 's' and szo[i + 2] == 'z') or (
                            szo[i] == 'z' and szo[i + 2] == 's') or (szo[i] == 't' and szo[i + 2] == 'y') or (
                            szo[i] == 'c' and szo[i + 2] == 's') or (szo[i] == 'd' and szo[i + 2] == 'z') or (
                            szo[i] == 'g' and szo[i + 2] == 'y') or (szo[i] == 'l' and szo[i + 2] == 'y'):
                        duplabetuvolt = 2
                        if szo[i] != szo[-i - 3] or szo[i + 2] != szo[-i - 1]:
                            palindrom = 0

                elif szo[i] == 'd' and szo[i + 1] == 'z' and szo[i + 2] == 's':
                    duplabetuvolt = 2
                    if szo[i] != szo[-i - 3] or szo[i + 1] != szo[-i - 2] or szo[i + 2] != szo[-i - 1]:
                        palindrom = 0

                else:
                    if (szo[i] == 'd' and szo[i + 1] == 'z' and szo[i + 2] != 's') or (
                            szo[i] == 'n' and szo[i + 1] == 'y') or (szo[i] == 's' and szo[i + 1] == 'z') or (
                            szo[i] == 'z' and szo[i + 1] == 's') or (szo[i] == 't' and szo[i + 1] == 'y') or (
                            szo[i] == 'c' and szo[i + 1] == 's') or (szo[i] == 'd' and szo[i + 1] == 'z') or (
                            szo[i] == 'g' and szo[i + 1] == 'y') or (szo[i] == 'l' and szo[i + 1] == 'y'):
                        duplabetuvolt = 1
                        if szo[i] != szo[-i - 2] or szo[i + 1] != szo[-i - 1]:
                            palindrom = 0

            else:
                if szo[i] != szo[-i - 1]:
                    palindrom = 0

    if palindrom == 1:
        print("Palindrom!")
    elif palindrom == 0:
        print("Nem palindrom!")


if __name__ == "__main__":
    main()

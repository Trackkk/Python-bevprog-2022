def hazi():
    bekert = input("Adj meg egy mondatot: ")
    lista = bekert.split(" ")
    dict = {}
    for i in bekert:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    # print(dict.keys())
    # print(dict.values())
    print("Betűk gyakorisága: ", dict)
    print("Fordítva: ", bekert[::-1])
    print("Listába rendezve szavanként: ", lista)
hazi()
def hazi2():
    number = input("Adjon meg egy számot és egy mértékegységet: (cm/inch):\n")
    unit = input()
    if unit == "cm":
        new = float(number)/2.54
        if float(new) % 1 == 0:
            print(int(new), "inches")
        else:
            print(new, "inches")
    elif unit == "inch":
        new = float(number)*2.54
        if float(new)%1 == 0:
            print(int(new), "cm")
        else:
            print(new, "cm")
    else:
        print("Not correct unit!")
hazi2()
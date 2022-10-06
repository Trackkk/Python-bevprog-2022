def hazi4():
    while True:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        finally:
            print("Out of try except blocks")
hazi4()
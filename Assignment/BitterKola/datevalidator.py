day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        if day >= 1 and day <= 30 and year > 0:
            print("Valid date")
        else:
            print("Invalid date")
    case 4 | 6 | 9 | 11:
        if day >= 1 and day <= 31 and year > 0:
            print("Valid date")
        else:
            print("Invalid date")
    case 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day >= 1 and day <= 29 and year > 0:
                print("Valid date")
            else:
                print("Invalid date")
        else:
           if day >= 1 and day <= 28 and year > 0:
                print("Valid date")
           else:
                print("Invalid date")
    case _:
        print("Invalid date")

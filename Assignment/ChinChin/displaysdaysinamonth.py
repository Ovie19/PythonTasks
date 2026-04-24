month = int(input("Enter month (1 - 12): "))
year = int(input("Enter year: "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("There are 31 days in the month")
    case 4 | 6 | 9 | 11:
        print("There are 30 days in the month")
    case 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("There are 29 days in the month")
        else:
           print("There are 28 days in the month")
    case _:
        print("Enter a valid number for month")

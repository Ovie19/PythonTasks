number = int(input("Enter a number (1 - 10): "))

match number:
    case 1:
        print("$1 --> one dollar")
    case 2:
        print("$2 --> two dollars")
    case 3:
        print("$3 --> three dollars")
    case 4:
        print("$4 --> four dollars")
    case 5:
        print("$5 --> five dollars")
    case 6:
        print("$6 --> six dollars")
    case 7:
        print("$7 --> seven dollars")
    case 8:
        print("$8 --> eight dollars")
    case 9:
        print("$9 --> nine dollars")
    case 10:
        print("$10 --> ten dollars")
    case _:
        print("Invalid response")

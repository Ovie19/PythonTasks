import random

random_number = random.randint(1, 7)

match random_number:
    case 1:
        print("Violet")
    case 2:
        print("Indigo")
    case 3:
        print("Blue")
    case 4:
        print("Green")
    case 5:
        print("Yellow")
    case 6:
        print("Orange")
    case 7:
        print("Red")
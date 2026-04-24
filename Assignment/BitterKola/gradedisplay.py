grade = input("Enter grade (A, B, C, D, or F): ")

match grade:
    case 'A':
        print("4.0 GPA")
    case 'B':
        print("3.0 GPA")
    case 'C':
        print("2.0 GPA")
    case 'D':
        print("1.0 GPA")
    case 'F':
        print("0.0 GPA")
    case _:
        print("Error: Invalid input")
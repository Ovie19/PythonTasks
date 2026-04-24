number = int(input("Enter a positive number: "))

number_square_root = number ** 0.5
casted_number_square_root = int(number_square_root)

if number_square_root == casted_number_square_root:
    print("It is a perfect square")
else:
    print("It is a not perfect square")

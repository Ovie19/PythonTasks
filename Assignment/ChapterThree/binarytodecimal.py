binary_number = int(input("Enter a binary number: "))
decimal_number = 0
count = 0

while binary_number > 0:
    remainder = binary_number % 10
    decimal_number += remainder * 2 ** count
    binary_number //= 10
    count += 1

print("The decimal equivalent is", decimal_number)
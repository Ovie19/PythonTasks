number = int(input("Enter a number: "))

if number % 4 == 0 and number % 5 == 0:
    print("The number is divisible by 4 and 5")
if number % 4 == 0 or number % 5 == 0:
    print("The number is divisible by 4 or 5")
if (number % 4 == 0 or number % 5 == 0) and (number % 4 != 0 or number % 5 != 0):
    print("The number is divisible by 4 or 5 but not by both")
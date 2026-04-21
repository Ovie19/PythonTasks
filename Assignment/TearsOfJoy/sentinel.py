"""
Initialize total to zero
Collect the number from user

While number is not equal to zero
    Add number to total
    Collect the number from user

Display value of total

"""


total = 0

number = int(input("Enter a number: "))

while number != 0:
    total += number
    number = int(input("Enter a number: "))

print("Total:", total)
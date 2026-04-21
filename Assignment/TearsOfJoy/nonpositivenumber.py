"""
Collect number from user
While number is not positive
    Collect number from user
else Display number
"""

number = int(input("Enter a number: "))

while number <= 0:
    number = int(input("Enter a number: "))
else:
    print("You entered:", number)
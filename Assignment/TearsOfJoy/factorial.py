"""
Collect number from user
Initialize factorial to one
for index in range from number to one
    factorial is equal to factorial multiplied by index

Display factorial
"""

number = int(input("Enter a number: "))

factorial = 1

for index in range(number, 0, -1):
    factorial *= index

print("Factorial:", factorial)
"""
For number in range of 1 to 50 inclusive
    If number is divisible by 3 and 5
        Display FizzBuzz
    Else if number is divisible by 3
        Display Fizz
    Else if number is divisible by 5
        Display Buzz
    Else
        Display number
"""

for index in range(1, 51):
    if index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz", end=" ")
    elif index % 3 == 0:
        print("Fizz", end=" ")
    elif index % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(index, end=" ")

print()
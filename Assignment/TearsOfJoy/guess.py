"""
Import random

Initialize random_number as a random number between 1 - 100 inclusive
Initialize count to zero

Collect user_input

while user_input is not equal to the user_input
    Increase count by 1
    if user_input is greater than the random_number:
        Display "Lower"
    if user_input is lesser than the random_number:
        Display "Higher"

    collect user_input

Display number of counts after loop ends

"""

import random

random_number = random.randint(1, 100)
count = 0

user_input = int(input("Enter a number: "))

while user_input != random_number:
    count += 1
    if user_input > random_number:
        print("Lower")
    if user_input < random_number:
        print("Higher")

    user_input = int(input("Enter a number: "))
else:
    print(f"{count} attempts")
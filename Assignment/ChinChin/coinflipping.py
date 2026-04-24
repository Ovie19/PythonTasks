import random

random_number = random.randrange(2)
user_number = int(input("Enter a number (0 - heads or 1 - tails): "))

if user_number == random_number:
    print("Your guess is correct")
else:
    print("Your guess is not correct")
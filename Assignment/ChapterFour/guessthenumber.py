import random

random_number = random.randint(1, 1000)
user_number = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

while random_number != user_number:
    if user_number > random_number:
        print("Too high. Try again.")
    elif user_number < random_number:
        print("Too low. Try again.")
    user_number = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

else:
    print("Congratulations. You guessed the number!")
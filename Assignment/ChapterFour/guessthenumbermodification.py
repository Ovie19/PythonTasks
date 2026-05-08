import random

random_number = random.randint(1, 1000)
count = 0
user_number = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

while random_number != user_number:
    count += 1
    if user_number > random_number:
        print("Too high. Try again.")
    elif user_number < random_number:
        print("Too low. Try again.")
    user_number = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

else:
    if count <= 10:
        print("Either you know the secret or you got lucky!")
    else:
        print("You should be able to do better!")
import random

def get_random_numbers():
    numbers = []
    numbers.append(random.randint(1, 9))
    numbers.append(random.randint(1, 9))
    return numbers

while True:
    numbers = get_random_numbers()
    product = numbers[0] * numbers[1]
    user_input = int(input(f"How much is {numbers[0]} times {numbers[1]}? "))

    while product != user_input:
        if product != user_input:
            print("No. Please try again.")
        user_input = int(input(f"How much is {numbers[0]} times {numbers[1]}? "))
    else:
        print("Very good!")

import random

def get_random_numbers(difficulty_level):
    numbers = []
    if difficulty_level == 1:
        numbers.append(random.randint(1, 9))
        numbers.append(random.randint(1, 9))
    else:
        numbers.append(random.randint(1, 99))
        numbers.append(random.randint(1, 99))
    return numbers

def get_correct_response():
    response_number = random.randrange(3)
    match response_number:
        case 0: return "Very good!"
        case 1: return "Nice work!"
        case 2: return "Keep up the good work!"

def get_wrong_response():
    response_number = random.randrange(3)
    match response_number:
        case 0: return "No. Please try again."
        case 1: return "Wrong. Try once more."
        case 2: return "No. Keep trying."

difficulty_level = int(input("1. Single-digits numbers\n2. Up to two-digits numbers\nEnter choice: "))
while True:
    numbers = get_random_numbers(difficulty_level)
    product = numbers[0] * numbers[1]
    user_input = int(input(f"How much is {numbers[0]} times {numbers[1]}? "))

    while product != user_input:
        if product != user_input:
            print(get_wrong_response())
        user_input = int(input(f"How much is {numbers[0]} times {numbers[1]}? "))
    else:
        print(get_correct_response())

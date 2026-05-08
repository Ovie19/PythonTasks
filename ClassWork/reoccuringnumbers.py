def get_reoccuring_numbers(numbers):
    reoccuring_numbers = []

    for number in numbers:
        count = 0
        for index in numbers:
            if index == number:
                count += 1

        if count > 1 and number not in reoccuring_numbers:
            reoccuring_numbers.append(number)

    return reoccuring_numbers
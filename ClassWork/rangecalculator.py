def calculate_range(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    return maximum - minimum

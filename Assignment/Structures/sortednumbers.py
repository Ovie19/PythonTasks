def display_sorted_numbers(first_number, second_number, third_number):
    highest = first_number
    mid = first_number
    lowest = first_number

    if first_number > second_number and first_number > third_number:
        highest = first_number

        if second_number > third_number:
            mid = second_number
            lowest = third_number
        else:
            mid = third_number
            lowest = second_number

    elif second_number > first_number and second_number > third_number:
        highest = second_number

        if first_number > third_number:
            mid = first_number
            lowest = third_number
        else:
            mid = third_number
            lowest = first_number

    elif third_number > first_number and third_number > second_number:
        highest = third_number

        if first_number > third_number:
            mid = first_number
            lowest = second_number
        else:
            mid = second_number
            lowest = first_number

    print(highest, mid, lowest)

first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))
display_sorted_numbers(first_number, second_number, third_number)

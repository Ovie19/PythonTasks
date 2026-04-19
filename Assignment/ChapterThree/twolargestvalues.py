number = int(input("Enter a number: "))
largest_number = number
second_largest_number = number

for index in range(9):
    number = int(input("Enter a number: "))
    if number > largest_number:
        second_largest_number = largest_number
        largest_number = number
    elif number > second_largest_number:
        second_largest_number = number

print("\nThe largest number is", largest_number)
print("The second largest number is", second_largest_number)
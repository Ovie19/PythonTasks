first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

sum_of_numbers = first_number + second_number + third_number
average = sum_of_numbers / 3
product = first_number * second_number * third_number

largest = first_number
smallest = first_number

# Largest number
if second_number > largest:
    largest = second_number
if third_number > largest:
    largest = third_number

# Smallest number
if second_number < smallest:
    smallest = second_number
if third_number < smallest:
    smallest = third_number


print("The sum of the numbers is", sum_of_numbers)
print("The product of the numbers is", product)
print("The average of the numbers is", average)
print("The largest number is", largest)
print("The smallest number is", smallest)

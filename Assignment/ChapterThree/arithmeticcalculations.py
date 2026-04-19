sum_of_numbers = 0
product_of_numbers = 1

for count in range(1, 5):
    number = int(input("Enter number: "))

    if count == 1:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    sum_of_numbers += number
    product_of_numbers *= number

average = sum_of_numbers / count

print("The sum of the numbers is", sum_of_numbers)
print("The product of the numbers is", product_of_numbers)
print("The average of the numbers is", average)
print("The largest number is", largest)
print("The smallest number is", smallest)

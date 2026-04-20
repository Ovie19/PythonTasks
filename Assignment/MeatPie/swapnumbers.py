first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

temp = second_number
second_number = first_number
first_number = temp

print("First number is", first_number)
print("Second number is", second_number)
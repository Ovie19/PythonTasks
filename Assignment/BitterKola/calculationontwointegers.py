first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if second_number > 0 and first_number > 0:
    print(f"{first_number} + {second_number} = {first_number + second_number}")
if second_number < 0 and first_number < 0:
    print(f"{first_number} x {second_number} = {first_number * second_number}")
else:
    if second_number > first_number:
        difference = second_number - first_number
    else :
        difference = first_number - second_number

    print("The difference is", difference)
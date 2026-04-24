number = int(input("Enter a three-digit number: "))
temporary_number = number

sum_of_its_digit = 0

while temporary_number > 0:
    sum_of_its_digit += temporary_number % 10
    temporary_number //= 10

if number % sum_of_its_digit == 0:
    print("It is divisible by the sum of its digits")
else:
    print("It is not divisible by the sum of its digits")
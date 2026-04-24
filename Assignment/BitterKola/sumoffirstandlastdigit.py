number = int(input("Enter a five-digit number: "))

first_digit = number // 10000
last_digit = number % 10

print(f"The sum of the first and last digit is {first_digit + last_digit}")
number = int(input("Enter a five-digit number: "))

fifth_digit = number % 10
number //= 10
fourth_digit = number % 10
number //= 10
third_digit = number % 10
number //= 10
second_digit = number % 10
number //= 10
first_digit = number % 10

print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)

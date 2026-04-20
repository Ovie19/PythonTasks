# Palindrome checker

number = int(input("Enter a five-digit integer: "))

fifth_digit = number % 10
number //= 10
fourth_digit = number % 10
number //= 10
third_digit = number % 10
number //= 10
second_digit = number % 10
number //= 10
first_digit = number % 10

if fifth_digit != first_digit or fourth_digit != second_digit:
    print("It is not a palindrome")
else:
    print("It is a palindrome")
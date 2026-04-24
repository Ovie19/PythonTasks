number = int(input("Enter an integer between 0 and 1000: "))
sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10

print("The sum of all its digits is", sum_of_digits)
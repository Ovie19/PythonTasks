number = int(input("Enter a three-digit integer: "))

third_digit = number % 10;
number //= 10;
second_digit = number % 10;
number //= 10;
first_digit = number % 10;

sum_of_digits = first_digit + second_digit + third_digit;
print(f"{first_digit} + {second_digit} + {third_digit} = {sum_of_digits}")

number = int(input("Enter a five-digit number: "))
separated_number_string = ""

while number > 0:
    remainder = number % 10
    number //= 10
    separated_number_string = f"{remainder} {separated_number_string}"

print(separated_number_string)

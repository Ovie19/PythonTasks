fraction_one_numerator = int(input("Enter fraction 1 numerator: "))
fraction_one_denominator = int(input("Enter fraction 1 denominator: "))

fraction_two_numerator = int(input("Enter fraction 2 numerator: "))
fraction_two_denominator = int(input("Enter fraction 2 denominator: "))

if fraction_one_denominator == 0 or fraction_two_denominator == 0:
    print("Denominator cannot be 0")
    exit

fraction_one = fraction_one_numerator / fraction_one_denominator
fraction_two = fraction_two_numerator / fraction_two_denominator

sum_of_fraction = fraction_one + fraction_two
difference = fraction_one - fraction_two
product = fraction_one * fraction_two
quotient = fraction_one / fraction_two

print("The sum of the fractions is", sum_of_fraction)
print("The difference of the fractions is", difference)
print("The product of the fractions is", product)
print("The quotient of the fractions is", quotient)

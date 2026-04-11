principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
number_of_years = int(input("Enter number of years: "))

simple_interest = (principal * rate * number_of_years) / 100
total_amount = simple_interest + principal

print("The interest on the principal is", simple_interest)
print("The total amount is", total_amount)

principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
duration_in_years = int(input("Enter the duration in years: "))

interest_rate /= 1200 
duration_in_months = duration_in_years * 12

monthly_payment_value = principal * (interest_rate * (1 + interest_rate) ** duration_in_months) / ((1 + interest_rate) ** duration_in_months - 1)

print("Your monthly payment is $" + str(monthly_payment_value))

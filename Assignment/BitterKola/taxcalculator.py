employee_salary = float(input("Enter employee's monthly salary: "))
monthly_tax = 0
if employee_salary > 600000:
   taxable_income = employee_salary - 600000
   employee_salary -= taxable_income
   monthly_tax += 0.25 * taxable_income

if employee_salary > 300000:
   taxable_income = employee_salary - 300000
   monthly_tax += 0.15 * taxable_income

annual_tax = monthly_tax * 12
print("Your monthly tax is", monthly_tax)
print("Your annual tax is", annual_tax)

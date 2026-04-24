birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year

if age >= 65:
    print("You are eligible for a senior citizen discount.")
else:
    print("You are not eligible for a senior citizen discount.")
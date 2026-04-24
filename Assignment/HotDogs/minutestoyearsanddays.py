total_minutes = int(input("Enter number of minutes: "))

total_days = total_minutes // 60 // 24
remainding_days = total_days % 365

total_year = total_days // 365

print(f"{total_year} year and {remainding_days} days")
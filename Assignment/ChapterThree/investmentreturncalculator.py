principal = 1000
rate = 7 / 100;

print("Year   Amount")
for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f"{year:>4}{amount:>10.2f}")
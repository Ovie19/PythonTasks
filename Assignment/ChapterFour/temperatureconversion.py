def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print("Celsius  Fahrenheit")
for celsius in range(101):
    print(f"{celsius:<9}{fahrenheit(celsius):.1f}")
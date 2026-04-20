# Average miles per gallon calculator

total_miles_driven = 0
total_gallon_used = 0
total_miles_per_gallon = 0

gallon_used = float(input("Enter the gallons used (-1 to end): "))
miles_driven = int(input("Enter the miles driven: "))
count = 0

while gallon_used != -1:
    total_gallon_used += gallon_used
    total_miles_driven += miles_driven

    miles_per_gallon = miles_driven / gallon_used
    total_miles_per_gallon += miles_per_gallon

    print(f"The miles/gallon for this tank was {miles_per_gallon:.6f}")

    count += 1
    gallon_used = float(input("Enter the gallons used (-1 to end): "))
    if (gallon_used == -1):
        break
    miles_driven = int(input("Enter the miles driven: "))

total_average_miles_per_gallon = total_miles_per_gallon / count
print(f"The overall average miles/gallon was {total_average_miles_per_gallon:.6f}")

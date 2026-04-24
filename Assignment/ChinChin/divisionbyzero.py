numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

if denominator != 0:
    result = numerator / denominator
    print(f"{numerator} / {denominator} = {result}")
else:
    print("Error: you cannot divide by 0");

packageWeight = int(input("Enter the weight of the package: "))

if 0 < packageWeight <= 2:
    print("The shipping cost is $2.5")
elif 2 < packageWeight <= 4:
    print("The shipping cost is $4.5")
elif 4 < packageWeight <= 10:
    print("The shipping cost is $7.5")
elif 10 < packageWeight <= 20:
    print("The shipping cost is $10.5")
else:
    print("The package cannot be shipped")

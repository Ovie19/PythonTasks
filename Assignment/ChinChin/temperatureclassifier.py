temperature = int(input("Enter a temperature: "))

if temperature < 0:
    print("Freezing")
elif temperature <= 15:
    print("Cold")
elif temperature <= 25:
    print("Warm")
else:
    print("Hot")
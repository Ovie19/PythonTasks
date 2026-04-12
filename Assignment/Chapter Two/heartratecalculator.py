user_age = int(input("Enter your age: "))

maximum_heart_rate = (220 - user_age)
minimum_target_heart_rate = maximum_heart_rate * 50 / 100
maximum_target_heart_rate = maximum_heart_rate * 85 / 100

print("Maximum heart rate is", maximum_heart_rate)
print("The target heart range is", minimum_target_heart_rate, "-",
    maximum_target_heart_rate)


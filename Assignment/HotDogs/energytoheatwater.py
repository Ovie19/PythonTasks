initial_temperature = int(input("Enter initial temperature: "))
final_temperature = int(input("Enter final temperature: "))
amount_of_water = int(input("Enter the amount of water in kilogram"))


energy = amount_of_water * (final_temperature - initial_temperature) * 4184
print("The energy required to heat the water is", energy)
take_off_speed = int(input("Enter the take-off speed: "))
acceleration = int(input("Enter the acceleration: "))

minimum_runway_length = take_off_speed ** 2 / (2 * acceleration)
print("The minimum runway needed is", minimum_runway_length)
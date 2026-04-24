initial_velocity = int(input("Enter initial velocity: "))
time = int(input("Enter time taken: "))
acceleration = int(input("Enter acceleration: "))

distance = initial_velocity * time + 0.5 * acceleration * time ** 2
print("The distance covered is ", distance)
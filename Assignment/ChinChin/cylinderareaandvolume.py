pi = 3.14159

height = float(input("Enter cylinder height: "))
radius = float(input("Enter cylinder radius: "))

surface_area = (2 * pi * radius) * (radius + height)
volume = pi * radius * radius * height

print("The surface area of the cylinder is", surface_area)
print("The volume of the cylinder is", volume)

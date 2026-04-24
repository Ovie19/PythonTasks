first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if abs(first_number) > abs(second_number):
    print("The second number is closer to zero")
elif abs(first_number) < abs(second_number):
    print("The first number is closer to zero")
else:
    print("Both are equally close to zero")
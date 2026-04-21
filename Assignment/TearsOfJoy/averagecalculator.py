"""
Collect a number from the user
Initialize count to zero
Initialize total to zero
While number is not equal to -1
    Increase count by 1
    Add number to total
    Collect a number from the user

If count is not zero
    Compute average as total / count
    Display average
"""

number = int(input("Enter a number (Enter -1 to exit): "))
count = 0
total = 0

while number != -1:
    count += 1
    total += number
    number = int(input("Enter a number (Enter -1 to exit): "))

if count != 0:
    average = total / count
    print(f"Average: {average}")
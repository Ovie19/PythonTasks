"""
Collect number from user
Initialize largest to number
while number is not "done"
    if number is greater than largest
        reassign number to largest
    Collect number from user

Display largest
"""

user_input = input("Enter a number (Enter done to exit): ")
largest = user_input

while user_input != "done":
    if user_input > largest:
        largest = user_input
    user_input = input("Enter a number (Enter done to exit): ")

print("Largest:", largest)
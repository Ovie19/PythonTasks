"""
Prompt user to enter input and store it
For index in range 1 to 10
    Display the value of user_input * index
"""

number = int(input("Enter a number: "))

for index in range(1, 11):
    product = number * index
    print(f"{number} x {index} = {product}")
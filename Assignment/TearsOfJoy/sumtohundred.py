"""
Initialize sum_of_numbers to zero
For number in range of 1 - 100 inclusive
    add number to sum_of_numbers

Display sum_of_numbers
"""

sum_of_numbers = 0

for number in range(1, 101):
    sum_of_numbers += number

print("The sum of 1 to 100 is", sum_of_numbers)
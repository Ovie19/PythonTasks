"""
Collect user_input
initialize reversed_string to empty string

for each character in user_input
    reversed_string = character + reversed_string

Display reversed_string
"""

user_input = input("Enter any word: ")
reversed_string = ""

for character in user_input:
    reversed_string = character + reversed_string

print("Reversed:", reversed_string)
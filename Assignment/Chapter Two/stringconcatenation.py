""" String concatenation using + adds both string together without adding extra space between them
    if first_name = "Emmanuel" and last_name = "Marks"
    first_name + last_name would give us "EmmanuelMarks"
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name
print("Welcome,", full_name)

""" The bug there is that the student assigned b to a without first storing the value of a, then
reassigned the value of a to b. By the end of this, both a and b would have the same value """

first_number = 5
second_number = 10

print("first number is", first_number, "and second number is", second_number)

temporary_value = first_number
first_number = second_number
second_number = temporary_value

print("first number is", first_number, "and second number is", second_number)

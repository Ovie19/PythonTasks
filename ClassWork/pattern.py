"""
Initialize number to 5
for count in range number to 1
    for index in range count to 1
        print index separated by a space
    print next line
"""

number = 5

for count in range(number, 0, -1):
    for index in range(count, 0, -1):
        print(index, end=" ")
    print()

# Validate user's input

"""
Initialize passes to zero
Initialize failures to zero
Initialize count to one

While count less than or equal to ten
    Input the next exam result
    If exam result is not equal to 1 or 2
        continue

    If the student passed
        Add one to passes
    Else
        Add one to failures

    Increase the count by one

Display the number of passes
Display the number of failures

If more than eight students passed
    Display “Bonus to instructor”
"""

passes = 0
failures = 0
count = 1

while count <= 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result != 1 and result != 2:
        continue

    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1

    count += 1

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

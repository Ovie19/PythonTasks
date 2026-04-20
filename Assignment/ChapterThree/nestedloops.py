"""
The outer loop runs 10 times, and the inner loops also runs 10 times.
The inner loops print < horizontally if the value of row is an even number
and also prints > horizontally if the row is an odd number
"""

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()

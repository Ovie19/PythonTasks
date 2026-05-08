def average(number, *args):
    return (sum(args) + number) / (len(args) + 1)

print(average(80, 88, 75, 96, 55, 83))
print(average(80))
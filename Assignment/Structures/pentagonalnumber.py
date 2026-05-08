def get_pentagonal_number(number):
    return int(number * (3 * number - 1) / 2);

for number in range(1, 101):
    pentagonal_number = get_pentagonal_number(number)
    print(f"{pentagonal_number:>7}", end="")

    if number % 10 == 0:
        print()
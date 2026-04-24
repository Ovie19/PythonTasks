print(f"{"Multiplication Table":^32}")

for number in range(10):
    if number != 0:
        print(number, end=" |   ")
    else:
        print(f"{"":>6}", end="")

    for multiplier in range(1, 10):
        if number != 0:
            print(f"{number * multiplier:>2}", end=" ")
        else:
            print(f"{multiplier:>2}", end=" ")
            if multiplier == 9:
                print("\n--------------------------------", end="")
    print()
print("ax + b = c")
a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
c = int(input("Enter the value c: "))

if a == 0:
    print("The equation has no unique solution")
else:
    result = (c - b) / a
    print(f"{a}x + {b} = {c}")
    print("x =", result);

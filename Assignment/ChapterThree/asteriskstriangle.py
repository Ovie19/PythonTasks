# Asterisks triangle

print("First Triangle")
for outer_loop_index in range(1, 11):
    for inner_loop_index in range(outer_loop_index):
       print("*", end="")

    print()

print("\nSecond Triangle")
count = 10
while count > 0:
    for inner_loop_index in range(count):
        print("*", end="")
    print()
    count -= 1

print("\nThird Triangle")
count = 10
while count > 0:
    for inner_loop_index in range(10, 0, -1):
        if inner_loop_index > count:
            print(" ", end="")
        else:
            print("*", end="")
    print()
    count -= 1

print("\nFourth Triangle")
#count = 0
#while count < 10:
#    for inner_loop_index in range(10, 0, -1):
#        if inner_loop_index < count:
#            print(" ", end="")
#        else:
#            print("*", end="")
#    print()
#    count += 1

# Pythagorean triples

for hypotenuse in range(1, 21):
    for side_one in range(1, 21):
        for side_two in range(1, 21):
            sum_of_two_sides_square = side_one * side_one + side_two * side_two
            hypotenuse_square = hypotenuse * hypotenuse
            if sum_of_two_sides_square == hypotenuse_square:
                print(f"Side 1 = {side_one:>2}, Side 2 = {side_two:>2}, Hypotenuse = {hypotenuse}")
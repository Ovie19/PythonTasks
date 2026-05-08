def product(*args):
    product = 1
    for number in args:
        product *= number

    return product

print(product(2, 3))
print(product(2, 3, 4))
print(product(2, 3, 4, 5))
print(product(2, 3, 4, 5, 6))
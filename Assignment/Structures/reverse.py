def reverse(number):
    reverse = 0
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10

    print(reverse)


number = int(input("Enter a number: "))
reverse(number)
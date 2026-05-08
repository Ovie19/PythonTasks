def reverse(number):
    reverse = 0
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    return reverse

def is_palindrome(number):
    return reverse(number) == number

number = int(input("Enter a number: "))
is_palindrome = is_palindrome(number)

if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
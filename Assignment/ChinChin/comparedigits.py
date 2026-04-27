number = int(input("Enter a two-digit integer: "))

unit = number % 10;
number //= 10;
tens = number % 10;

if tens > unit:
    print("Tens digit is greater than unit digit");
elif tens < unit:
    print("Tens digit is lesser than unit digit");
else:
    print("Tens digit is equal to unit digit")
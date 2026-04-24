user_pin = int(input("Enter your PIN: "))

if 1000 <= user_pin <= 9999:
    print("Valid PIN")
else:
    print("Invalid PIN")
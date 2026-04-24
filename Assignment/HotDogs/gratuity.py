subtotal = int(input("Enter subtotal: "))
gratuity_rate = int(input("Enter gratuity rate: "))

gratuity = subtotal * gratuity_rate / 100
total = subtotal + gratuity

print("Gratuity:", gratuity)
print("Total:", total)
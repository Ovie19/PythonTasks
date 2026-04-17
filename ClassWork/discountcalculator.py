"""
Collect purchase amount from user

If the purchase amount is less than 1000
    print no discount and print the price
    
Else if the purchase amount is between 1000 and 10000
    calculate discount using purchase amount * 0.05
    calculate price after discount
    print the price 
    
Else if the purchase amount is between 10000 and 50000
    calculate discount using purchase amount * 0.1
    calculate price after discount
    print the price 
    
Else  
    calculate discount using purchase amount * 0.2
    calculate price after discount
    print the price 
"""

purchase_amount = int(input("Enter amount: "))

if purchase_amount < 1000:
    print("No discount", "Your price is", purchase_amount)
elif 1000 <= purchase_amount <= 10000:
    discount = purchase_amount * 0.05
    price = purchase_amount - discount
    print("The new price is", price)
elif 10000 < purchase_amount <= 50000:
    discount = purchase_amount * 0.1
    price = purchase_amount - discount
    print("The new price is", price)
else:
    discount = purchase_amount * 0.2
    price = purchase_amount - discount
    print("The new price is", price)

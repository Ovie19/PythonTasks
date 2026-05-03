from pybank import *

message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit  """

while True:
    print(message)
    user_input = input("Choose an option: ")
    match user_input:
        case "1":
            email = input("Enter a valid email address: ")
            password = input("Enter a strong password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration unsuccessful")

        case "2":
            email = input("Enter a valid email address: ")
            password = input("Enter a strong password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login unsuccessful")

        case "3":
            transactions = []
            amount = float(input("Enter transactions or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter transactions or 0 to stop: "))
            total_balance = calculate_balance(transactions)
            print("total balance is", total_balance)

        case "4":
            balance = float(input("Enter balance: "))
            rate = float(input("Enter rate: "))
            years = int(input("Enter number of years: "))
            interest = apply_interest(balance, rate, years)
            print("Your interest is", interest)

        case "5":
            transactions = []
            transaction_type = input("1. Credit\n2. Debit\nEnter transaction type: ")
            transaction = int(input("Enter transactions or 0 to stop: "))
            while transaction != 0:
                if transaction_type == "1":
                    transactions.append(["credit", transaction])
                    print("shsh")
                else:
                    transactions.append(["debit", transaction])

                transaction_type = input("1. Credit\n2. Debit\nEnter transaction type: ")
                transaction = int(input("Enter transactions or 0 to stop: "))

            transaction_summary = get_transaction_summary(transactions)
            print("\nTransaction summary")
            print("Total credit:", transaction_summary[0][1])
            print("Total debit:", transaction_summary[1][1])
            print("Net balance:", transaction_summary[2][1])
            print("Transaction count:", transaction_summary[3][1])

        case "6":
            break

    print()

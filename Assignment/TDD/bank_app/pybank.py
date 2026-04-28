def validate_email(email):
    if len(email) >= 8 and email.find("@") != -1:
        if not email.startswith("@") and not email.endswith("@"):
            return True

    return False

def calculate_balance(transactions):
    if len(transactions) == 0:
        return 0

    total = 0
    for transaction in transactions:
        total += transaction

    return total

def is_strong_password(password):
    if len(password) >= 8:
        return True

    return False

def apply_interest(balance, rate, years):
    if rate < 0 or years < 1:
        return 0

    interest = balance * (1 + rate / 100) ** years

    return round(interest, 2);

def get_transaction_summary(transactions):
    credits = 0
    debits = 0
    count = len(transactions)

    for transaction in transactions:
        if transaction[0] == "credit":
            credits += transaction[1]
        else:
            debits += transaction[1]

    balance = credits - debits
    return [["total_credits", credits], ["total_debits", debits], ["net_balance", balance], ["transaction_count", count]]
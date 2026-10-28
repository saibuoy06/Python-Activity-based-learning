balance = 5000
withdrawal_limit = 10000

transactions = [
    ("deposit", 2000),
    ("withdraw", 1500),
    ("withdraw", 7000),
    ("deposit", 1000),
    ("withdraw", 12000)
]

successful = 0
rejected = 0

print("Initial Balance: ₹", balance)

for transaction, amount in transactions:

    if amount <= 0:
        print(transaction, amount, "- Invalid Amount")
        rejected += 1

    elif transaction == "deposit":
        balance += amount
        print("Deposit: ₹", amount, "- Successful")
        successful += 1

    elif transaction == "withdraw":
        if amount > withdrawal_limit:
            print("Withdrawal: ₹", amount, "- Limit Exceeded")
            rejected += 1

        elif amount > balance:
            print("Withdrawal: ₹", amount, "- Insufficient Balance")
            rejected += 1

        else:
            balance -= amount
            print("Withdrawal: ₹", amount, "- Successful")
            successful += 1

    else:
        print("Invalid Transaction")
        rejected += 1

print("\n--- Transaction Summary ---")
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)
print("Final Balance: ₹", balance)

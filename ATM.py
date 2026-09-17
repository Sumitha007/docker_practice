balance = 10000

print("===== ATM =====")

print("Initial Balance:", balance)

# Deposit
amount = 5000
balance += amount
print("Amount deposited:", amount)

# Withdraw
amount = 2000

if amount <= balance:
    balance -= amount
    print("Amount withdrawn:", amount)
else:
    print("Insufficient balance.")

print("Final Balance:", balance)

print("ATM process completed.")
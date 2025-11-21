balance=1000
amount=int(input("Enter the amount: "))
if amount >0:
    balance += amount
    print("Balance after deposite:",balance)
else:
    print("Invalid amount")
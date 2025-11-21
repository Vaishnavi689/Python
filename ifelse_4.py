
balance=1000
amount=int(input("Enter the amount:"))
if amount >0 and amount <= balance:
    balance -= amount
    print("Balance after withdraw :",balance)

else:
    print("Invalid amount or insufficient balance")
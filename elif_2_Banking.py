# Banking Application
# Deposite , Withdraw , Balance Exit
pin = 1212
userpin = int(input("Enter your pin: "))
         

if userpin == pin:
    print("Verified Pin...✅")
    print("------Welcome to SBI Bank------")
    print("""
    1. Deposit
    2. Withdraw
    3. Balance Check
    4. Exit
    """)

    choice = int(input("Enter your choice: "))
    balance = 5000

    if choice == 1:
        deposit = float(input("Enter the amount to be deposited: "))

        if deposit > 0:
            balance += deposit
            print("Rs", deposit, "has been deposited successfully")
            print("Updated Balance:", balance)
        else:
            print("Invalid Amount")

    elif choice == 2:
        withdraw = float(input("Enter the amount to withdraw: "))

        if withdraw > 0 and withdraw <= balance:
            balance -= withdraw
            print("Rs", withdraw, "has been withdrawn successfully")
            print("Updated Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Your Balance is Rs:", balance)

    elif choice == 4:
        print("Thank you for banking with us..!")
        print("Thank you for using our Application")

    else:
        print("Invalid Choice")

else:
    print("Invalid Pin... ❌")

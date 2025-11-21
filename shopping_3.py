print("Welcome to the Shopping Application")
print("""
       1. Electronics 
       2. Clothings
       3. Groceries
       4. Exit
""")

choice = int(input("Enter your choice: "))

price = 0   # To avoid undefined variable error

# -------------------- ELECTRONICS --------------------
if choice == 1:
    print("""
         1. Mobile (25k)
         2. Laptop (45k)
         3. TV (12k)
         4. Exit
    """)
    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        price = 25000
        print("You have selected Mobile.")
    elif choice1 == 2:
        price = 45000
        print("You have selected Laptop.")
    elif choice1 == 3:
        price = 12000
        print("You have selected TV.")
    elif choice1 == 4:
        print("Thank you!")
        exit()
    else:
        print("Invalid choice")
        exit()

# -------------------- CLOTHING --------------------
elif choice == 2:
    print("""
         1. Women Kurti Set (1000)
         2. Gents Wear (1500)
         3. Western Dress (2000)
         4. Exit
    """)
    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        price = 1000
        print("You have selected Women Kurti Set.")
    elif choice2 == 2:
        price = 1500
        print("You have selected Gents Wear.")
    elif choice2 == 3:
        price = 2000
        print("You have selected Western Dress.")
    elif choice2 == 4:
        print("Thank you!")
        exit()
    else:
        print("Invalid choice")
        exit()

# -------------------- GROCERIES --------------------
elif choice == 3:
    print("""
         1. Sugar (50)
         2. Rice (100)
         3. Wheat (40)
         4. Exit
    """)
    
    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        price = 50
        print("You have selected Sugar.")
    elif choice3 == 2:
        price = 100
        print("You have selected Rice.")
    elif choice3 == 3:
        price = 40
        print("You have selected Wheat.")
    elif choice3 == 4:
        print("Thank you!")
        exit()
    else:
        print("Invalid choice")
        exit()

# -------------------- EXIT OPTION --------------------
elif choice == 4:
    print("Exit")
    print("Thanks for using Shopping Application!")
    exit()

else:
    print("Invalid Choice")
    exit()


# -------------------- BILL CALCULATION --------------------
quantity = int(input("Enter the quantity: "))
total = price * quantity

# Discount logic
discount = 0

if total > 10000:
    discount = total * 0.20
    print("You got 20% discount:", discount)
elif total > 5000:
    discount = total * 0.10
    print("You got 10% discount:", discount)
else:
    print("No Discount")

finalAmount = total - discount
print("Your Final Amount is:", finalAmount)
print("You got Discount Rs:", discount)
print("Do visit again...! Thank You!")

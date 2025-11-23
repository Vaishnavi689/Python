# ATM Application
# I want to check pin 3 times
# after 3 attemps blocked the user

pin = int(input("Enter your pin:"))
 
attempt=0
balance=10000
while attempt<3:
    if pin==1234:
        print("Welcome to ATM")
        while True:
            print("1.Balance Enquiry:")
            print("2.Withdraw cash:")
            print("3.Deposite Cash:")
            print("4.Exit:")
            choice = int(input("Enter your choice:"))

            if choice==1:
                print("Your Balance is:",balance )
            elif choice==2:
                amount = int(input("Enter the amount to withdraw: "))
                if amount >0:
                    if amount <=amount:
                        balance-=amount
                        print("Withdraw amount sucessfully....New Balance is:",balance)
                    else:
                      print("Insufficient Balance")
                else:
                    print("Invalid Amount")
            elif choice==3:
                amount=int(input("Enter the amount to Deposite :"))
                if amount>0:
                    balance+=amount
                    print("Deposite Sucessfully..New Balance is ",balance)
                else:
                    print("Invalid Amount")
            elif choice==4:
                print("Thank you for using ATM")
                break
                
            else:
                print("Invalid choice")
        break
    else:
        print("Invalid pin")
        attempt+=1
        if attempt==3:
            print("Your Account is Blocked")
            break
        pin =int(input("Enter your pin:"))
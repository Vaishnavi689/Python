# number which is divisible by 1 and itself called as prime numbers

num=int(input("Enter a number: "))

if num >1:
    for i in range(2,num): # range is start from 2 because 1 is not prime number 
        if num% i==0:
            print("Its not a prime number")
            break
    else:  # we can write else for forloop also
        print("Prime Number")
else:
    print("Please Enter number greater than 1 ")

    


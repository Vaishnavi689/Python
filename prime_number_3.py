# addition of prime number
total=0
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        total+=i
print("The sum of price numbers between 1 to 100 is:",total)
# print all numbers which are divisible by 3 and 5 and add this numbers 

total=0
for i in range(1,100):
    if i%3==0 and i % 5==0:
        total=total +i
print(total)
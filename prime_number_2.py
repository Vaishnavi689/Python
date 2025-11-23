# print all prime numbers from 1 to 100
              #2<100
for i in range(2,101): #101-1=100
                 #2<2 false hence print else block i=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
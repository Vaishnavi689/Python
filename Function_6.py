# code for prime number

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

prime(5)

print("======================================================")

def add():
    return 10*10 ,10+10,10-10,10/10
x,y,a,b=add()
print(x)
print(y)
print(a)
print(b)

print("============================================================")

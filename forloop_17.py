# I want 1 st row as @ 3rd row as # and 5th row as 0

for i in range(1,6):
    for j in range(1,6):
        if i==1:
            print("@", end=" ")
        elif j==5:
            print("0",end=" 4")
        elif i==3:
            print("#",end=" ")
        elif i==5:
            print("$",end=" ")
        else:
            print("*", end=" ")
    print("\n")
        
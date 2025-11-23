#  I want # on 3rd row and remaining *

for i in range(1, 6):
    for j in range(1, 6):
        if i == 3:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()   # move to next line after each row

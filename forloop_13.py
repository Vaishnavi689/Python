# Print tables from 2 to 30 
# first for loop for rows
# 2nd for loop for column

for i in range(2, 31):      # Outer loop → table number
    print(f"\nTable of {i}") 
    print("----------------")

    for j in range(1, 11):  # Inner loop → 1 to 10
        print(i, "x", j, "=", i * j)

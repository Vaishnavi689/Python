i = 1
count = 0
total_sum = 0

while i <= 100:
    if i % 5 == 0 and i % 10 == 0:
        print(i)
        count += 1
        total_sum += i   # add the actual number
    i += 1

print("Total count of numbers divisible by 5 and 10:", count)
print("Total sum of numbers divisible by 5 and 10:", total_sum)

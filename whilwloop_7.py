i = 1
count = 0
total_sum = 0

while i <= 100:
    if i % 3 == 0:
        print(i)
        count += 1
        total_sum += i
    i += 1

print("Total count of numbers divisible by 3 from 1 to 100:", count)
print("Sum of all numbers divisible by 3 from 1 to 100:", total_sum)

i = 1
count = 0

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        count += 1
    i += 1   # increment i properly

print("Total count of numbers divisible by both 3 and 5 from 1 to 100:", count)

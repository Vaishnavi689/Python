# print total sum from 1 to 100 even numbers

i = 1
total = 0

while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

print("Total sum of even numbers from 1 to 100:", total)

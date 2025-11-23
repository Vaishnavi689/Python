number = int(input("Enter the number: "))

reverse = 0

while number > 0:        # number greater than 0
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

print("Reversed Number:", reverse)

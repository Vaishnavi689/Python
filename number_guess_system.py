import random

number = random.randint(1, 100)


# give 3 attemps only to guess the number
print("You have 3 attempts to guess the number")

print("Guess the number between 1 to 100")
attempts = 3
for i in range(attempts+1):
    guess = int(input("Enter Your Guess :"))
    
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("You guessed it right!")
        print("You took", attempts, "attempts.")
        break
else:
    print(f"You have executed all your attempts.The number was {number}")
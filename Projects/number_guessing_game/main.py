import random
print("Welcome to Number Guessing Game!")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")
choice = input("Choose Difficulty (1/2/3): ")
if choice == "1":
    maximum = 50
elif choice == "2":
    maximum = 100
else:
    maximum = 500
secret = random.randint(1, maximum)
attempt = 0
while True:
    try:
        guess = int(input(f"Enter your Guess (1-{maximum}): "))
        attempt += 1
        if guess < secret:
            print("Too Low!")
        elif guess > secret:
            print("Too High!")
        else:
            print("Congratulations!")
            print("Attempts:", attempt)
            break
    except ValueError:
        print("Please enter a valid number!")
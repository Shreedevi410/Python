import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid choice!")
    attempts = 0

while attempts > 0:

    print(f"\nYou have {attempts} attempts remaining.")

    guess = int(input("Make a guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number!")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

    attempts -= 1

if attempts == 0:
    print(f"You are out of attempts! The number was {number}.")

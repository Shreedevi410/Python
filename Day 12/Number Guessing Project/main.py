from random import randint
from art import logo


EASY_TURNS = 10
HARD_TURNS = 5
attempts = 0

def check_answer(user_guess, actual_answer,attempts):
    if user_guess < actual_answer:
        print("Its too less")
        return  attempts - 1
    elif user_guess > actual_answer:
        print("its too high")
        return attempts - 1
    else:
        print(f"Hey you guessed correct number {actual_answer}")

def set_difficulty():
    level = input("you want to go with easy or hard").lower()
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print(logo)
    print("Welcome to the number guessing game")
    user_number = int(input("choose number between 1 to 100"))
    answer = randint(1, 100)
    while user_number != answer
    check_answer(user_number,answer)
    turns= set_difficulty()
    print("")


game()
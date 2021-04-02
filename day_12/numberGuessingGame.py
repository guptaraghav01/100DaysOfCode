import random
from art import logo

easy_level_turns = 10
hard_level_turns = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print(logo)
    print("Welcome to the number gussing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        elif guess != answer:
            print("Guess Agian.")


game()

# Output
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀███░▄▄▄█░██░█░▄▄█░▄▄█░▄▄█░▄▄█░▄▄▀
# █░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄███░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀█░▄▄█░▀▀▄
# █▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄███▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄█▄▄▄█▄█▄▄
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

# Welcome to the number gussing game!
# I'm thinking of a number between 1 and 100.
# Choose difficulty. Type 'easy' or 'hard': easy
# You have 10 attempts remaining to guess the number.
# Male a guess: 50
# Too high
# Guess Agian.
# You have 9 attempts remaining to guess the number.
# Male a guess: 25
# Too high
# Guess Agian.
# You have 8 attempts remaining to guess the number.
# Male a guess: 12
# Too high
# Guess Agian.
# You have 7 attempts remaining to guess the number.
# Male a guess: 6
# You got it! The answer was 6.

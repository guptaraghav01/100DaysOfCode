import random

flag = True
guess = None
count = 1

upper_limit = int(input("Enter an upper limit: \n"))

secret = random.randint(1, upper_limit)

while guess != secret:
    guess = input(f"Please type a number between 1 and {upper_limit}: ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("You got it.")
    else:
        if guess < secret:
            print("Go higher.")
        else:
            print("Go lower.")
        count += 1

print('')

# Output
# Enter an upper limit: 
# 20
# Please type a number between 1 and 20: 10
# Go higher.
# Please type a number between 1 and 20: 15
# Go lower.
# Please type a number between 1 and 20: 12
# Go higher.
# Please type a number between 1 and 20: 13
# You got it.
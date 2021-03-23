from art import logo, vs
from gameData import data
import random
import os


def format_data(account):
    """Format the account data returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Comapare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')  # Clear screen
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right!✅Current Score:{score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong!❌Final Score:{score}")


# Output

#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# Comapare A: Neymar, a Footballer from Brasil

#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)

# Against B: UEFA Champions League, a Club football competition from Europe
# Who has more followers? Type 'A' or 'B': a

#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# You're right!✅Current Score:1
# Comapare A: UEFA Champions League, a Club football competition from Europe

#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)

# Against B: Kourtney Kardashian, a Reality TV personality from United States
# Who has more followers? Type 'A' or 'B': b

#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# You're right!✅Current Score:2
# Comapare A: Kourtney Kardashian, a Reality TV personality from United States

#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)

# Against B: Kendall Jenner, a Reality TV personality and Model from United States
# Who has more followers? Type 'A' or 'B': a

#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/

# Sorry, that's wrong!❌Final Score:2

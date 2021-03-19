import random
from art import logo


def deal_card():
    """
    return a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 😑"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack! 😱"
    elif user_score == 0:
        return "Win with a blackjack! 🤑"
    elif user_score > 21:
        return "You went over. You Lose! 😢"
    elif computer_score > 21:
        return "Opponent went over. You Win! 🤩"
    elif user_score > computer_score:
        return "You Win! 😎"
    else:
        return "You Lose! 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_shoud_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_shoud_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}.")
    print(
        f"Computer's final score: {computer_cards}, final score: {computer_score}.")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack. Type 'y' or 'n': \n") == "y":
    play_game()


# Output
# Do you want to play a game of blackjack. Type 'y' or 'n':
# y

# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
#       |  \/ K|                            _/ |
#       `------'                           |__/

# Your cards: [10, 9], current score: 19
# Computer's first card: 8
# Type 'y' to get another card, type 'n' to pass: n
# Your final hand: [10, 9], final score: 19.
# Computer's final score: [8, 5, 2, 2], final score: 17.
# You Win! 😎
# Do you want to play a game of blackjack. Type 'y' or 'n':
# n

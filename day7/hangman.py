import random
from hangman_words import word_list
from hangman_arts import stages, logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guesses {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The correct word was {chosen_word}.")
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

# Output

#  _
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/

# Guess a letter: a
# _ a _ a _

#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========

# Guess a letter: b
# You guessed b, that's not in the word.You lose a life.
# _ a _ a _

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# Guess a letter: l
# You guessed l, that's not in the word.You lose a life.
# _ a _ a _

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# Guess a letter: k
# k a _ a k

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# Guess a letter: y
# k a y a k
# You win.

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

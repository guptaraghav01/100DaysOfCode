import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

print(options[user_choice])

print("Computer chose:\n")
computer_choice = random.randint(0,2)
print(options[computer_choice])

if user_choice == computer_choice:
    print("Draw!")
elif user_choice == 0:
    if computer_choice == 1:
        print("You lose.")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    else:
        print("You lose.")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose.")
    else:
        print("You win!")


# Output
# What do you choose?
# Type 0 for Rock, 1 for Paper or 2 for Scissors.
# 1

#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)

# Computer chose:


#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

# You win!
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lowercase_string = combined_string.lower()

t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')

true = t + r + u + e

l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')

love = l + o + v + e

message = ""

love_score = str(true) + str(love)

int_love_score = int(love_score)

if int_love_score < 10 or int_love_score > 90:
    message = ", you go together like coke and mentos."
elif int_love_score > 40 and int_love_score < 50:
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {love_score}%{message}")


# Output
# Welcome to the Love Calculator!
# What is your name?
# kanye west
# What is their name? 
# kim kardashian
# Your score is 42%, you are alright together.

# Welcome to the Love Calculator!
# What is your name?
# prince harry
# What is their name? 
# meghan markle
# Your score is 74%.
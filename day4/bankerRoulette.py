import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(',')
num_names = len(names)

index = random.randint(0, num_names - 1)
personWhoWillPay = names[index]
print(f"{personWhoWillPay} is going to buy the meal today!")

# Output
# Give me everybody's names, separated by a comma. ben,anthony,charles,karl
# charles is going to buy the meal today!
from art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))

    bids[name] = price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)


# Output

#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\
#                        .-------------.
#                       /_______________\

# What is your name?
# michael
# What is your bid?
# $500
# Are there any other bidders? Type 'yes' or 'no'.
# yes
# What is your name?
# james
# What is your bid?
# $480
# Are there any other bidders? Type 'yes' or 'no'.
# yes
# What is your name?
# tim
# What is your bid?
# $420
# Are there any other bidders? Type 'yes' or 'no'.
# no
# The winner is michael with a bid of $500.
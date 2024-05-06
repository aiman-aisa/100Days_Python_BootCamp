from art import logo
import os
print(logo)

bid_again = True
bid_dict = {}

while bid_again:
    name = input("What is your name?:   ")
    bid = int(input("What is your bid?:   $"))
    highest_bidder = ""
    highest_bid = 0
    bid_dict[name] = bid
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if another_bid == "no":
        bid_again = False
        for key, value in bid_dict.items():
            if value > highest_bid:
                highest_bid = value
                highest_bidder = key
    else:
        os.system('cls')
        
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")



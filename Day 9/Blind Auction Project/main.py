# TODO-1: Ask the user for input
from art import logo
print(logo)

def highest_bid(bidder_dict):
    higest_price = 0
    winner = ""
    for bidder in bidder_dict:
        bid_amount = bidder_dict[bidder]
        if bid_amount > higest_price:
            higest_price = bid_amount
            winner = bidder
    print(f"Winner is {winner} and he got it for {higest_price}")


# TODO-2: Save data into dictionary {name: price}
bid_dict = {}


# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
continue_bidding = True
while continue_bidding:
    name = input("What is your name?")
    price = int(input("What is your bid?"))
    bid_dict[name] = price
    option = input("If anyone are there who wants to bid? Yes or no").lower()
    if option == "no":
        continue_bidding = False
        highest_bid(bid_dict)
    elif option == "yes":
        print("\n " * 20)





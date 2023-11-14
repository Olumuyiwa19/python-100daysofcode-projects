### Bidding Game #####

bids = {}

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_finished = False

while not bidding_finished:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'? \n")

    if more_bids == "no":
        bidding_finished = True
        highest_bidder(bids)

from replit import clear
import art

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the Blind Aution!")
participants = {}
more_participants = True


def winning_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bider_name in bidding_record:
        if bidding_record[bider_name] > highest_bid:
            highest_bid = bidding_record[bider_name]
            winner = bider_name

    print(f"Winner of the Blind Auction is {winner} with a bid price of £{highest_bid}")


while more_participants == True:

    name = input("What is your Name?: ")
    bid = int(input("What is your bid?: £"))

    participants[name] = bid

    more = input("Are there more participants in the auction? Y or N ").lower()
    if more == "n":
        more_participants = False
        winning_bidder(participants)

    elif more == "y":
        clear()


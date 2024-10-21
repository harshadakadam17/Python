def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    # Find the highest bid and winner
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bid_details = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your Name? ")
    bid = int(input("What is your bid? $"))  # Convert bid to an integer
    bid_details[name] = bid  # Store the bid in the dictionary

    should_continue = input("Are there any other bidders? Type 'Yes' or 'No': \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bid_details)  # Call function with the bid_details dictionary
    elif should_continue == "yes":
        print("\n" * 100)  # Clear screen (simulated by printing new lines)

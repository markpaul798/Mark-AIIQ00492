# Define the accepted denominations and the price of a Coke
Denominations = [25, 10, 5]
Price = 50

# Initialize the amount inserted and the change owed
Amount_inserted = 0
Change = 0

# Keep prompting for input until enough money has been inserted
While amount_inserted < price:
    # Prompt the user to insert a coin
    Coin = int(input(“Insert a coin (25, 10, or 5 cents): “))

    # Check if the coin is an accepted denomination
    If coin in denominations:
        # Update the amount inserted and the amount due
        Amount_inserted += coin
        Change = price – amount_inserted

        # Inform the user of the amount due
        Print(“Amount due: {} cents”.format(change))
    Else:
        # Ignore the input if it’s not an accepted denomination
        Print(“Invalid coin. Accepted denominations are 25, 10, and 5 cents.”)

# Output the change owed
Print(“Change owed: {} cents”.format(change))









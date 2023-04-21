From collections import Counter

Grocery_list = []
While True:
    Try:
        Item = input(“Enter an item to add to your grocery list: “)
    Except EOFError:  # catch control-d (EOF) input to end the loop
        Break
    Grocery_list.append(item.lower())  # convert item to lowercase before adding to the list

# count the occurrences of each item in the list
Counter = Counter(grocery_list)

# sort the items alphabetically and output the list
For item, count in sorted(counter.items()):
    Print(f”{count} {item.upper()}”)


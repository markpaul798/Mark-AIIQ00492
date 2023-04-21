MENU = {
    “Baja Taco”: 4.00,
    “Burrito”: 7.50,
    “Bowl”: 8.50,
    “Nachos”: 11.00,
    “Quesadilla”: 8.50,
    “Super Burrito”: 8.50,
    “Super Quesadilla”: 9.50,
    “Taco”: 3.00,
    “Tortilla Salad”: 8.00
}

Order_total = 0.00

While True:
    Try:
        Item = input(“Enter an item (or ctrl-d to finish): “).title()
    Except EOFError:
        Break

    If item not in MENU:
        Continue

    Order_total += MENU[item]
    Print(f”Total cost: ${order_total:.2f}”)

Print(f”Final total: ${order_total:.2f}”)


Greeting = input(“Please enter a greeting: “)

# Strip leading whitespace from the greeting
Greeting = greeting.lstrip()

# Check if the greeting starts with “hello”
If greeting.lower().startswith(“hello”):
    Print(“$0”)
# Check if the greeting starts with an “h” (but not “hello”)
Elif greeting.lower().startswith(“h”):
    Print(“$20”)
# Otherwise, output $100
Else:
    Print(“$100”)


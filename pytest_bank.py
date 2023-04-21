Def value(greeting):
    # Convert the greeting to lowercase for case-insensitive matching
    Greeting = greeting.lower()

    # Check if the greeting starts with “hello”
    If greeting.startswith(“hello”):
        Return 0

    # Check if the greeting starts with “h” (but not “hello”)
    Elif greeting.startswith(“h”):
        Return 20

    # Return 100 for any other greeting
    Else:
        Return 100


Def main():
    # Prompt the user for a greeting
    Greeting = input(“Enter a greeting: “)

    # Calculate the value of the greeting
    Print(“The value of the greeting is:”, value(greeting))


If __name__ == “__main__”:
    Main()


From bank import value


Def test_value_hello():
    Assert value(“Hello, world!”) == 0
    Assert value(“hello there”) == 0


Def test_value_h():
    Assert value(“hi there”) == 20
    Assert value(“hey, how are you?”) == 20


Def test_value_other():
    Assert value(“goodbye”) == 100
    Assert value(“howdy”) == 100
    Assert value(“hELLO, wORLD!”) == 0
    Assert value(“greetings”) == 100


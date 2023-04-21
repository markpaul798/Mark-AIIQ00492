Import random

While True:
    Level_str = input(“Enter the level (1-100): “)
    Try:
        Level = int(level_str)
        If level > 0 and level <= 100:
            Break
    Except ValueError:
        Pass
    Print(“Invalid input. Please enter a positive integer between 1 and 100.”)

Secret_number = random.randint(1, level)

While True:
    Guess_str = input(“Guess the number (1-{}): “.format(level))
    Try:
        Guess = int(guess_str)
        If guess <= 0 or guess > level:
            Raise ValueError
    Except ValueError:
        Print(“Invalid input. Please enter a positive integer between 1 and {}.”.format(level))
        Continue

    If guess < secret_number:
        Print(“Too small!”)
    Elif guess > secret_number:
        Print(“Too large!”)
    Else:
        Print(“Just right!”)
        Break

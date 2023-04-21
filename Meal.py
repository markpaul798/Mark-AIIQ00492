Def convert(time):
    “””Converts a time in 24-hour format to the corresponding number of hours as a float.”””
    Hours, minutes = time.split(“:”)
    Return float(hours) + float(minutes) / 60

Def main():
    “””Prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.”””
    Time = input(“Please enter a time in 24-hour format (e.g. 7:30): “)
    Hours = convert(time)

    If 7 <= hours < 8:
        Print(“It’s breakfast time!”)
    Elif 12 <= hours < 13:
        Print(“It’s lunch time!”)
    Elif 18 <= hours < 19:
        Print(“It’s dinner time!”)

If __name__ == “__main__”:
    Main()


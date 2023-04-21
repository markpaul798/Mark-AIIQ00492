Def main():
    While True:
        Try:
            Fraction = input(“Enter the fuel gauge fraction (X/Y): “)
            X, y = map(int, fraction.split(‘/’))
            If x <= 0 or y <= 0 or x > y:
                Raise ValueError
            Break
        Except (ValueError, ZeroDivisionError):
            Print(“Invalid input. Please try again.”)

    Percent = int(x / y * 100 + 0.5)

    If percent <= 1:
        Print(“E”)
    Elif percent >= 99:
        Print(“F”)
    Else:
        Print(percent, “%”)


If __name__ == ‘__main__’:
    Main()


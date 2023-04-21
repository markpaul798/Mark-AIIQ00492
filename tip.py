Def main():
    Dollars = dollars_to_float(input(“How much was the meal? “))
    Percent = percent_to_float(input(“What percentage would you like to tip? “))
    Tip = dollars * percent
    Print(f”Leave ${tip:.2f}”)


Def dollars_to_float(d):
    Return float(d.strip(“$”))


Def percent_to_float(p):
    Return float(p.strip(“%”)) / 100


Main()



Def main():
    Camel_case = input(“Enter a variable name in camel case: “)
    Snake_case = “”
    For I, char in enumerate(camel_case):
        If I == 0:
            Snake_case += char.lower()
        Elif char.isupper():
            Snake_case += “_” + char.lower()
        Else:
            Snake_case += char
    Print(“The variable name in snake case is:”, snake_case)


If __name__ == “__main__”:
    Main()


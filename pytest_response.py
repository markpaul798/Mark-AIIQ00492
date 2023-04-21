Pip install validators

Import validators

Def main():
    Email = input(“Please enter your email address: “)
    If validators.validate_email(email):
        Print(“Valid”)
    Else:
        Print(“Invalid”)
        
If __name__ == “__main__”:
    Main()


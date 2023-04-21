Import sys
Import requests


Def main():
    # Check if the number of Bitcoins argument is provided
    If len(sys.argv) != 2:
        Print(“Usage: python bitcoin.py <number of Bitcoins>”)
        Sys.exit(1)

    # Convert the argument to a float
    Try:
        Num_bitcoins = float(sys.argv[1])
    Except ValueError:
        Print(“Error: Invalid number of Bitcoins”)
        Sys.exit(1)

    # Query the API for the current Bitcoin price
    Try:
        Response = requests.get(https://api.coindesk.com/v1/bpi/currentprice.json)
        Response.raise_for_status()
        Data = response.json()
        Price = float(data[“bpi”][“USD”][“rate”].replace(“,”, “”))
    Except requests.RequestException:
        Print(“Error: Failed to retrieve Bitcoin price”)
        Sys.exit(1)
    Except (KeyError, ValueError):
        Print(“Error: Invalid response from API”)
        Sys.exit(1)

    # Calculate the total cost in USD
    Cost = num_bitcoins * price

    # Print the result with thousands separator and four decimal places
    Print(f”{num_bitcoins:.8g} Bitcoin(s) is currently worth ${cost:,.4f}”)


If __name__ == “__main__”:
    Main()



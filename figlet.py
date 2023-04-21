Import sys
Import argparse
Import pyfiglet

# set up command-line argument parsing
Parser = argparse.ArgumentParser()
Parser.add_argument(‘-f’, ‘—font’, help=’name of the font to use’)
Args = parser.parse_args()

# if the font argument was provided, validate it
If args.font:
    Available_fonts = pyfiglet.FigletFont.getFonts()
    If args.font not in available_fonts:
        Sys.exit(f’Error: “{args.font}” is not a valid font. Available fonts: {available_fonts}’)

# prompt the user for a string of text
Text = input(‘Enter some text to display: ‘)

# create a Figlet object with the specified font (or a random font)
Figlet = pyfiglet.Figlet(font=args.font)

# output the text in the chosen font
Print(figlet.renderText(text))


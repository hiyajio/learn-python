from pyfiglet import figlet_format as figform
from termcolor import colored as col

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

phrase = input("What message do you want to print? ")
shade = input("What color? ")

if shade not in valid_colors:
    shade = "blue"

text = col(figform(phrase), color=shade)
print(text)
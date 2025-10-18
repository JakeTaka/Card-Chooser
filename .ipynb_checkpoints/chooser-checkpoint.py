import os
import sys

decklist_exists = input("""Hello and welcome to my Card Chooser project.
                        Do you have your decklist in a .txt file that follows 
                        a format like:
                        1 Ephemerate
                        1 Soulherder
                        1 Momentary Blink...
                        (Yes/No)?""")

if decklist_exists.lower() == 'yes':
    filename = input("Great! Please put that file in the folder this script is in and provide me the name of the file: ")
else:
    print("I'm sorry but that is what's required for this program to run. Please come back once you're finished")
    sys.exit()

with open(filename,'r') as file:
    decklist =file.read()

cards = decklist.split("\n")
#deck_dict = dict(card.split(" ") for card in cards)
i = 0

for card in cards:
    while i<1:
        print(card)
        i+=1
#print(deck_dict)

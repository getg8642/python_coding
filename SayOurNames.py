# SayOurNames.py

# Ask the user for their name

name = input("What is your name? ")

# keep  printing names until we want to quit

while name != "":
    # print their name 100 times
    for x in range(100):
        # print their name followed by a space,not a new line
        print(name,end=" ")
    print()  # After the for loop ,skip down to the next line
    # Ask for another name ,or quit
    name = input("Type another name,or just hit [Enter] to quit: ")
{print("Thanks for playing!!")}

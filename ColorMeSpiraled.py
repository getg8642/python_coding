# ColorSpiralInput.py - prints a colorful spiral of the input content

import turtle # Set up turtle  graphics


t = turtle

t.bgcolor("black")


# Set up a list of any 8 valid python color names

colors = ["red","blue","green","yellow","orange","purple","white","gray"]


# Ask the user for their name
your_name = t.textinput("Enter your name","What is your name?")

# Ask the user for the number of sides,between 1 and 8,with a default of 4
sides = int(t.numinput("Number of sides","How many sides do you want (1-8)?",4,1,8))



# Draw a colorful spiral with the user-specified number of sides

for x in range(120):
    t.pencolor(colors[x % sides])  # Only use the right number of colors
    t.penup()
    t.forward(x * 3 /sides + x)    # Change the size to match number of sides
    t.pendown()
    t.write(your_name,font = ("Arial",int((x + 8) / 6),"bold"))
    t.left(360 / sides + 5)        # Turn 360 degrees / number of sides,plus1
    

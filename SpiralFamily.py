# SpiralFamily.py

import turtle

t = turtle

t.bgcolor("black")

colors = ["red","blue","yellow","green","orange","purple","white","brown","gray","pink"]

family = []   # set a empty list for the family names


# Ask for the first name

name = t.textinput("My family","Enter a name,or just hit [Enter] to end:")

# Keep asking for names

while name != "":
    
    # Add their name to the family list
    
    family.append(name)

    # Ask for another name ,or end

    name = t.textinput("My family","Enter a name,or just hit [Enter] to end:")


# Draw a spiral of the names on the screen

for x in range(100):
    
    t.pencolor(colors[x%len(family)])  # rotate through the colors
    
    t.penup()    # Don't draw the regular spiral lines
    
    t.forward(x*4)   # Just move the turtle on the screen
    
    t.pendown()    # Draw the next family member's name
    
    t.write(family[x%len(family)],font = ("宋体",int((x+4)/4),"bold"))
    
    t.left(360/len(family) +2 )     # Turn left for our spiral              

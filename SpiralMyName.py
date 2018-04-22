# SpiralMyName,py - prints a colorful spiral of the user's name

import turtle # Set up turtle  graphics


t = turtle

t.bgcolor("black")

colors = ["red","blue","green","yellow"]


# Ask the user's name using turtle's textinput pop-up window

your_name = t.textinput("Enter your name","What is your name?")

# Draw a spiral of the name on the screen,written 100 times

for x in range(100):
    t.pencolor(colors[x%4])  # rotate through the four colors
    t.penup()       # Don't draw  the regular spiral lines
    t.forward(x*4) # Just move the turtle on the screen
    t.pendown       # Writes the user's name,bigger each time
    t.write(your_name,font = ("Arial",int((x + 8) / 4),"bold"))
    t.left(95)      # Turn left ,just as in our other spirals

# RosetteGoneWild

import turtle

# define a turtle object for named t
t=turtle

# define the backgroud color
t.bgcolor("black")
# Ask the user for the number of circles in their rosette,default to 6
number_of_circles = int(t.numinput("Number of circles","How many circles in your rosette?",6,3,1000))
for x in  range(number_of_circles):
    t.pencolor("red")  # define the pen color
    t.circle(100)
    t.left(360/number_of_circles)

t.left(360/number_of_circles/2) 
for x in  range(number_of_circles):
    t.pencolor("purple")  # define the pen color
    t.circle(75)
    t.left(360/number_of_circles)
    
t.left(360/number_of_circles/2) 
for x in  range(number_of_circles):
    t.pencolor("green")  # define the pen color
    t.circle(50)
    t.left(360/number_of_circles)

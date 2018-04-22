# squareSpiral3.py

import turtle
colors = ["red","yellow","blue","green"]
t=turtle
t.bgcolor("black")
## 
for x in range(250):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
    

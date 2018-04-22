# ColorSpiral.py

import turtle

t=turtle
colors = ["red","yellow","blue","green","orange","Purple","pink","salmon"]
t.bgcolor("black")
#sides = 6
#sides = 5
#sides = 4
#sides = 3
#sides = 2

sides = 8
## 
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides +1)
    t.width(x*sides/200)
    

from turtle import *

pensize(3)
pencolor("Maroon")

begin_fill()
fillcolor("Sienna")

forward(50)
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
end_fill()

penup()
left(90)
forward(50)
pendown()

pencolor("DarkGreen")
begin_fill()
fillcolor("ForestGreen")

for i in range(3):
    right(120)
    forward(150)
end_fill()    

penup()
right(120)
forward(150)
left(120)
forward(75)
pendown()
pencolor("DarkGreen")
begin_fill()
fillcolor("ForestGreen")
for i in range(3):
    right(120)
    forward(150)
end_fill()



done()
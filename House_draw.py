from turtle import *
speed(0)
bgcolor("ForestGreen")

penup()
goto(-400,-100)
pendown()

fillcolor("DeepSkyBlue")
begin_fill()
for i in range(2) :
    forward(800)
    left(90)
    forward(450)
    left(90)
end_fill()

penup()
goto(-320,225)
pendown()
pencolor("Yellow")
fillcolor("Yellow")
begin_fill()
circle(35)
end_fill()

penup()
goto(200,200)
pendown()
pencolor("White")
fillcolor("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(220,240)
pendown()
fillcolor("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(230,215)
pendown()
fillcolor("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(180,225)
pendown()
fillcolor("White")
begin_fill()
circle(25)
end_fill()

penup()
goto(-100,-100)
pendown()

pensize(3)
pencolor("Chocolate")
fillcolor("DarkOrange")
begin_fill()
for i in range(4) :
    forward(170)
    left(90)
end_fill()

penup()
goto(20,130)
pendown()
pencolor("Brown")
fillcolor("SaddleBrown")
begin_fill()
for i in range(2) :
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

penup()
goto(-127,70)
pendown()
#pencolor("Sienna")
#fillcolor("Peru")
begin_fill()

for i in range(3) :
    forward(225)
    left(120)
end_fill()

penup()
goto(0,0)
pendown()
pencolor("black")
fillcolor("white")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(0,25)
pendown()
pencolor("black")
forward(50)

penup()
goto(25,0)
pendown()
left(90)
forward(50)

penup()
goto(-80,0)
pendown()
right(90)
pencolor("black")
fillcolor("white")
begin_fill()

for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(-80,25)
pendown()
pencolor("black")
forward(50)

penup()
goto(-55,0)
pendown()
left(90)
forward(50)

penup()
goto(-40,-97)
pendown()
right(90)
#pencolor("white")
fillcolor("black")
begin_fill()
for i in range(2) :
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

penup()
goto(-30,-60)
pendown()
fillcolor("white")
begin_fill()
circle(8)
end_fill()

hideturtle()


done()
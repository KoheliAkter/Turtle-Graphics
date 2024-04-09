from turtle import*

shape("turtle")
#circle
pensize(5)
pencolor("DarkRed")
begin_fill()
fillcolor("Orange")
circle(100)
end_fill()

#squar
penup()
forward(200)
pendown()

pensize(5)
pencolor("OrangeRed")
begin_fill()
fillcolor("LightSalmon")

left(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

#triangle
penup()
forward(450)
pendown()

pensize(5)
pencolor("Yellow")
begin_fill()
fillcolor("DarkKhaki")

for i in range(3):
    forward(200)
    right(120)
end_fill()

#Hexagons and Octagons
penup()
forward(200)
left(90)
forward(200)
pendown()

pensize(5)
pencolor("Purple")
begin_fill()
fillcolor("MediumSpringGreen")

for i in range(8):
    forward(100)
    right(45)
end_fill()
#rectangle
penup()
left(90)
forward(200)
pendown()

pensize(5)
pencolor("Green")
begin_fill()
fillcolor("DarkSeaGreen")

forward(300)
right(90)
forward(190)
right(90)
forward(300)
right(90)
forward(190)
end_fill()


penup()
forward(100)
right(90)
forward(500)
pendown()

pensize(5)
pencolor("Cyan")
begin_fill()
fillcolor("DarkCyan")

forward(50)
right(90)
forward(200)
right(90)
forward(50)
right(90)
forward(200)
end_fill()

done()

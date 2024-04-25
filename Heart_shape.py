from turtle import *

import turtle
vr = turtle.Turtle()

#set the Back Ground color
turtle.Screen().bgcolor('black')
turtle.pensize(4)
vr.speed (20)

def drawcurve():
    for i in range(200):
        vr.right(1)
        vr. forward(1)
        
vr.color('red')
vr.begin_fill()
vr.left(140)

 # Draw the left line
vr.forward(111.65)
drawcurve()
vr.left(120)
drawcurve()
 # Draw the right line
vr.forward(111.65)
vr.end_fill()
vr.penup()
vr.goto(77, -40)
vr.pendown()
vr.hideturtle()









done()
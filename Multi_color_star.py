from turtle import *

import turtle
t= turtle.Turtle()
screen=turtle.Screen()
t.speed(30)
color=("Red","Blue","Green","White","Yellow","Purple")
screen.bgcolor("black")

for i in range(100):
    t.color(color[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)


done()
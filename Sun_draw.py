from turtle import *

import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0) 

def draw_sunray(length):
    t.color("yellow")
    t.forward(length)
    t.backward(length)

num_rays = 50
ray_length = 200

for _ in range(num_rays):
    draw_sunray(ray_length)
    t.left(360 / num_rays)

t.penup()
t.goto(0, 0)
t.dot(100, "yellow")


t.hideturtle()
screen.mainloop()

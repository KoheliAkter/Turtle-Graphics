from turtle import *

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Trek")
screen.setup(width=600, height=600)
screen.bgcolor("skyblue")

# Create player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Define movement functions
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

# Close the window when clicked
screen.mainloop()


done()
from turtle import *

import turtle
import random

# Function to generate color
def generate_color():
    colors = ['OrangeRed', 'Red', 'Yellow', 'Purple', 'Blue', 'Maroon', 'Fuchsia']
    return random.choice(colors)

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.setup(width=800, height=600)
screen.bgcolor("ForestGreen")

# Create racetrack border
border = turtle.Turtle()
border.speed(0)
border.color("black")
border.penup()
border.setposition(-380, -280)
border.pensize(3)
border.pendown()
for _ in range(2):
    border.forward(760)
    border.left(90)
    border.forward(560)
    border.left(90)
border.hideturtle()

# Create finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.color("red")
finish_line.pensize(5)
finish_line.goto(370, -270)
finish_line.pendown()
finish_line.goto(370, 270)

# Create racers
racers = []
turtle_names = ["player-1", " player-2", " player-3", " player-4", " player-5"]
for name in turtle_names:
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.penup()
    racer.goto(-350, -250 + turtle_names.index(name) * 100)
    color = generate_color()
    racer.color(color, color)
    racer.speed(random.randint(1, 10))
    racer.write(name, align="center", font=("Courier", 12, "normal"))
    racers.append(racer)

# Race loop
winner = None
while True:
    for racer in racers:
        racer.forward(random.randint(1, 20))
        if racer.xcor() >= 350:
            winner = racer.color()[0]
            break
    if winner:
        break

# Display winner
text = turtle.Turtle()
text.speed(0)
text.color("black")
text.penup()
text.hideturtle()
text.goto(0, 0)
text.write(f"The winner is the {winner} turtle!", align="center", font=("Courier", 24, "normal"))

screen.mainloop()

done()
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=500)

X = 500
Y = 500

number_turtle = int(screen.textinput(title="Number of Turtle's", prompt="How many Turtle are in the race?"))
factor = (Y - 50) / number_turtle
value = -((number_turtle-1) * factor) / 2
for _ in range(number_turtle):
    timmy = Turtle(shape="turtle")
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.color(color)
    timmy.penup()
    timmy.setpos(x=(-X/2)+20, y=value)
    value += factor

bet = int(screen.textinput(title="Place your bet!", prompt="Which turtle will win the race, enter a number starting from top."))
screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

width = int(screen.textinput(title="Width", prompt="What will be the Length of the race track?"))
height = int(screen.textinput(title="Height", prompt="What will be the Width of the race track?"))

screen.setup(width=width, height=height)

X = width
Y = height

number_turtle = int(screen.textinput(title="Number of Turtle's", prompt="How many Turtle are in the race?"))


def race_start():
    factor = (Y - 50) / number_turtle
    value = -((number_turtle-1) * factor) / 2

    for _ in range(number_turtle):
        timmy = Turtle(shape="turtle")
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.color(color)
        timmy.penup()
        timmy.setpos(x=(-X/2)+20, y=value)
        value += factor

    my_turtles = screen.turtles()
    bet = int(screen.textinput(title="Place your bet!", prompt="Which turtle will win the race, enter a number starting from bottom."))

    winner = False

    while not winner:
        current_turtle = random.randint(0, number_turtle-1)
        if my_turtles[current_turtle].xcor() >= ((X/2)-20):
            winner = True
            if (current_turtle+1) == bet:
                print("Yaay 🎆 your turtle won the race!!")
                screen.bye()
            else:
                print("On no your turtle lost 😔")
                screen.bye()
        else:
            rand_distance = random.randint(0, 10)
            my_turtles[current_turtle].forward(rand_distance)


race_start()

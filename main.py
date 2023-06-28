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
    bet = int(screen.textinput(title="Place your bet!", prompt="Which turtle will win the race, enter a number starting from top."))

    for _ in range(number_turtle):
        timmy = Turtle(shape="turtle")
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.color(color)
        timmy.penup()
        timmy.setpos(x=(-X/2)+20, y=value)
        value += factor

        if timmy.xcor() > ((X/2)-20):
            print(timmy.color())
        else:
            rand_distance = random.randint(0, 10)
            timmy.forward(rand_distance)

race_start()
screen.exitonclick()





# while is_race_on:
    # for turtle in all_turtles:
    #     #230 is 250 - half the width of the turtle.
    #     if turtle.xcor() > 230:
    #         is_race_on = False
    #         winning_color = turtle.pencolor()
    #         if winning_color == bet:
    #             print(f"You've won! The {winning_color} turtle is the winner!")
    #         else:
    #             print(f"You've lost! The {winning_color} turtle is the winner!")
    #
    #     #Make each turtle move a random amount.
    #     rand_distance = random.randint(0, 10)
    #     turtle.forward(rand_distance)
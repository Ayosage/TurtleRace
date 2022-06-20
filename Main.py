from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput("Make your bet", "Which turtle will win the race: Enter a color")

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]

# create a turtle for each color
for color in colors:
    pcu = color
    color = Turtle("turtle")
    color.pu()
    color.color(pcu)
    turtles.append(color)






# send turtle to start position on left side of screen
def start_positions():
    z = (screen.window_height() / len(colors))
    x = -240
    y = 180
    for _ in turtles:
        _.setpos(x, y)
        y -= z

# random movements forward
def race():
    for _ in turtles:
        _.fd(random.randint(0, 20))

#check if anyone crossed the finish line and if user guess was correct
def check_postition():
    for _ in turtles:
        if _.xcor() >= 240:
            print(_.xcor(), _.pencolor())
            if user_guess.lower() == _.pencolor():
                print(f"You win! {_.pencolor()} won the race!")
            else:
                print(f"You lose, {_.pencolor()} won the race!")
            return _.xcor()
    return 0


start_positions()

while check_postition() < 240:
    race()

screen.exitonclick()

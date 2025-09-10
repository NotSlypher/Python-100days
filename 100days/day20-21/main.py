import time
from turtle import Turtle, Screen
from naagin import Naagin

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("day20-21-snake-game")
screen.tracer(0)

naagin = Naagin()

screen.listen()
screen.onkey(naagin.left, "Left")
screen.onkey(naagin.right, "Right")
screen.onkey(naagin.up, "Up")
screen.onkey(naagin.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    naagin.move()




screen.exitonclick()






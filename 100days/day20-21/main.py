import time
from encodings.punycode import segregate
from turtle import Turtle, Screen
from naagin import Naagin
from food import Food
from scoreboard import Scoreboard

FOOD_DISTANCE= 15
WALL = 275

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("day20-21-snake-game")
screen.tracer(0)

naagin = Naagin()
food = Food()
scoreboard = Scoreboard()

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
    if naagin.head.distance(food) < FOOD_DISTANCE:
        food.refresh()
        naagin.extend()
        scoreboard.score_up()

    # wall hit game end
    if naagin.head.xcor() >= WALL or naagin.head.xcor() <= -WALL \
            or naagin.head.ycor() >= WALL or naagin.head.ycor() <= -WALL:
        is_game_on=False
        scoreboard.game_over()

    #detect self collision
    for segment in naagin.naagin[1:]:
        if segment.distance(naagin.head) < 10:
            is_game_on=False
            scoreboard.game_over()


screen.exitonclick()






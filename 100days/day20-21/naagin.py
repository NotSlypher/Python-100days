from socket import send_fds
from turtle import Turtle
MOVE_DISTANCE = 20
LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270

class Naagin:
    def __init__(self):
        self.naagin: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.naagin[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(i * -20, 0)
            self.naagin.append(segment)

    def move(self):
        for seg_num in range(len(self.naagin) - 1, 0, -1):
            xcor = self.naagin[seg_num - 1].xcor()
            ycor = self.naagin[seg_num - 1].ycor()
            self.naagin[seg_num].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


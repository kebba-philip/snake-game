from turtle import Turtle, down
from constants import STARTING_POSITIONS, MOVE_DISTANCE
from constants import UP, DOWN, RIGHT, LEFT

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment in range(len(self.segments) - 1 , 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

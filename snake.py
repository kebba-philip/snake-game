from turtle import Turtle
from constants import STARTING_POSITIONS, MOVE_DISTANCE

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        for segment in range(len(self.segments) - 1 , 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.segments[0].fd(MOVE_DISTANCE)

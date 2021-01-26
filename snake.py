import turtle as t
from turtle import Turtle
from random import randrange
STARTING_POSITION = [(0, 0), (-25, 0), (-50, 0)]
MOVE_DISTANCE = 25
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

t.colormode(255)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("dim gray")
            # new_segment.color(
            #     (randrange(120, 128), randrange(120, 128), randrange(120, 128)))
            new_segment.penup()
            new_segment.shapesize(stretch_len=1.25, stretch_wid=1.25)
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("dim gray")
        # new_segment.color(
        #     (randrange(120, 128), randrange(120, 128), randrange(120, 128)))
        new_segment.penup()
        new_segment.shapesize(stretch_len=1.25, stretch_wid=1.25)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(position=self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

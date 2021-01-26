from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.65, stretch_wid=0.65)
        self.color("black")
        self.penup()
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        random_location = (random_x, random_y)
        self.goto(random_location)

    def refresh(self):
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        random_location = (random_x, random_y)
        self.goto(random_location)

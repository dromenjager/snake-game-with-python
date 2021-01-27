from turtle import Turtle
import random


class Food(Turtle):
    """
    Class for the food
    for snake
    """
    def __init__(self):
        """
        Initialize the
        Food object
        """
        super().__init__()
        """
        Inherit turtle class
        attributes and methods
        """
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # rand_x = random.randint(-280, 280)
        # rand_y = random.randint(-280, 280)
        # self.goto(rand_x, rand_y)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        move the food to
        random position in
        the game display
        """
        x_ = random.randint(-280, 280)
        y_ = random.randint(-280, 280)
        self.goto(x_, y_)

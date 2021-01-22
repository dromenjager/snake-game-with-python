from turtle import Turtle, Screen
import time
POSITION = [(0.0, 0.0), (-20.0, 0.0), (-30.0, 0.0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """
    Create a snakes object
    """
    def __init__(self):
        """
        initiate snake
        instance
        """
        super().__init__()
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        """
        create the actual object
        """
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add segments to snake body"""
        new_snake = Turtle(shape="square")  # new object
        new_snake.color("green")  # set color
        new_snake.penup()  # don't draw connecting lines
        new_snake.setpos(position)  # set position of each snake
        self.snakes.append(new_snake)  # add to the snake list

    def extend_seg(self):
        """Add new segment to snake body"""
        self.penup()
        self.add_segment(self.snakes[-1].position())

    def move(self, game_on=True):
        """
        control the movement of the snake
        """
        for idx in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[idx-1].xcor()
            new_y = self.snakes[idx-1].ycor()
            # move the last piece to previous ones's position
            self.snakes[idx].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        move the snake
        forward
        move head up , others follow
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        move the snake down,
        move head down , others follow
        """
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

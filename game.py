# import libraries
import turtle as t
import random
import time
from snakes import Snake
from food import Food
from score import Score


# setup screen dims
screen = t.Screen()
screen.setup(width=600, height=600)
# change the screen background color
screen.bgcolor("black")
# set the title of the app
screen.title("Snake game")
# Fixing animation glitches - using tracer object
screen.tracer(0)


# Create snake object
snakes = Snake()
# Create food object
food = Food()
# Screen tracks key-press
screen.listen()

# move forward:
screen.onkey(snakes.up, "Up")
# move backward:
screen.onkey(snakes.down, "Down")
# move left:
screen.onkey(snakes.left, "Left")
# move right:
screen.onkey(snakes.right, "Right")

# Create a Scoreboard
scoreboard = Score()

game_on = True  # Game is enabled

while game_on:
    screen.update()  # refresh screen
    time.sleep(0.1)  # delay in refreshing the screen
    snakes.move()

    # Detect snake's collision with food
    if snakes.head.distance(food) < 15:
        food.refresh()  # move the snake to new position
        snakes.extend_seg()
        scoreboard.increase_score()

    # Game Over when Snake collides with Walls:
    if (snakes.head.xcor() > 280 or snakes.head.xcor() < -280) or\
            (snakes.head.ycor() > 280 or snakes.head.ycor() < -280):
        scoreboard.game_over()
        game_on = False


# Keep screen alive till click
screen.exitonclick()

from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    """
    Create the Scoreboard
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        # self.msg = msg
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGN,
                   font=FONT)
        self.hideturtle()
        self.speed("fastest")

    def game_over(self):
        """
        New message for game-over
        """
        self.goto(0.0, 0.0)
        return self.write("Game Over", align=ALIGN,
                          font=FONT)

    def increase_score(self):
        """
        Increment the score
        """
        self.score += 1
        self.clear()
        return self.write(f"Score : {self.score}", align=ALIGN,
                          font=FONT)

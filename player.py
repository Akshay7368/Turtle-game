
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("arial", 24, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.....", font=FONT, align="center")

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

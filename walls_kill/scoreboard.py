"""
Module containing all items relating to the scoreboard objects in the game.
"""

# Imports
from turtle import Turtle


# Class
class Scoreboard(Turtle):
    """
    Scoreboard class that inherits from Turtle class from which scoreboard objects can be created.
    """
    def __init__(self):
        """
        Upon instantiation inherit Turtle class.
        """
        super().__init__()
        self.score = 0
        self.high_score = 0

    def create(self, position, text_1, text_2):
        """
        Checks if 'self.score is greater than 'self.high_score', if True updates 'self.high_score'.
        Creates custom scoreboard at 'position', displaying 'text_1', 'text_2', 'self.score' and 'self.high_score'.
        Where:
        'position' = user defined coordinate as a tuple.
        'text_1' and 'text_2' = user defined string of text to display.
        """
        if self.score > self.high_score:
            self.high_score = self.score
        x, y = position
        self.clear()
        self.penup()
        self.goto(x, y)
        self.pencolor("white")
        self.write(f"{text_1}: {self.score}  {text_2}: {self.high_score}", False, align="center",
                   font=("arial", 15, "normal"))
        self.hideturtle()



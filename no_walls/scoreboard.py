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

    def create(self, position, points, text):
        """
        Creates custom scoreboard at 'position', showing 'points', and displaying 'text'.
        Where:
        'position' = user defined coordinate as a tuple.
        'points' = 'score'.
        'text' = user defined string of text to display.
        """
        x, y = position
        self.clear()
        self.penup()
        self.goto(x, y)
        self.pencolor("white")
        self.write(f"{text}: {points}", False, align="center", font=("arial", 15, "normal"))
        self.hideturtle()

    def game_over(self, position):
        """
        Creates scoreboard at 'position' displaying 'GAME OVER'.
        """
        x, y = position
        self.clear()
        self.penup()
        self.goto(x, y)
        self.pencolor("white")
        self.write("GAME OVER", False, align="center", font=("arial", 25, "normal"))
        self.hideturtle()

    def food_eaten(self, position):
        """
        Creates scoreboard at 'position' displaying 'GAME OVER'.
        """
        x, y = position
        self.clear()
        self.penup()
        self.goto(x, y)
        self.write("NOM NOM", False, align="center", font=("arial", 30, "normal"))
        self.hideturtle()



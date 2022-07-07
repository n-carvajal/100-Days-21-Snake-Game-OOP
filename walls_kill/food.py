"""
Module containing all items relating to the food objects in the game.
"""

# Imports
from turtle import Turtle
from random import randrange

# Constants
FOOD_GROWTH_FACTOR = 0.5


# Class
class Food(Turtle):
    """
    Food class that inherits from Turtle class from which food objects can be created.
    """
    def __init__(self):
        """
        Upon instantiation inherit Turtle, assign attributes and call spawn() method.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("red")
        self.turtlesize(FOOD_GROWTH_FACTOR)

    def spawn(self):
        """
        Method that places the food object at a random position.

        Uses randint() to generate a position within the Turtle bounds of -380 to 380 for both 'x' and 'y'.
        Then inputs that position into 'self.goto()'.
        """
        self.goto(randrange(-380, 380, 20), randrange(-380, 380, 20))
        self.showturtle()

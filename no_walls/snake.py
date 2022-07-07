"""
Module containing all items related to the snake.
"""

# Imports
from turtle import Turtle

# Constants
SNAKE_STARTING_LENGTH = 2
SNAKE_HEAD_STARTING_POSITION = (0, 0)
SNAKE_GROWTH_FACTOR = 1
DEFAULT_SEGMENT_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DARK_GREEN = (27, 94, 32)
LIGHT_GREEN = (56, 142, 60)


# Class
class Snake(Turtle):
    """
    Snake class from which snake objects can be created.
    """
    def __init__(self):
        """
        Upon instantiation of a Snake object, the Turtle class is inherited and the following attributes are defined.
        """
        super().__init__()
        self.segments = []

    def spawn(self):
        """
        Creates the starting snake body.

        Creates 'length' quantity of Turtle() objects each called 'segment'.
        Each 'segment' is assigned a set of attributes (penup, color, shape, and turtlesize).
        The first 'segment' created is placed at 'x_pos, y_pos' on the screen.
        Subsequent 'segment' objects are moved left on the 'X' axis by DEFAULT_SEGMENT_SIZE * SNAKE_GROWTH_FACTOR.
        Every created 'segment' is appended to the list at 'self.segments'.
        """
        x_pos, y_pos = SNAKE_HEAD_STARTING_POSITION
        for n in range(SNAKE_STARTING_LENGTH):
            segment = Turtle()
            segment.penup()
            if n % 2 == 0:
                segment.color(DARK_GREEN)
            else:
                segment.color(LIGHT_GREEN)
            segment.shape("square")
            segment.turtlesize(SNAKE_GROWTH_FACTOR)
            segment.goto(x_pos, y_pos)
            self.segments.append(segment)
            x_pos -= (DEFAULT_SEGMENT_SIZE * SNAKE_GROWTH_FACTOR)

    def move(self):
        """
        Moves the Turtle segments in 'self.segments' forward by increments of DEFAULT_SEGMENT_SIZE.

        It does so by moving the last segment in self.segments to the position of the second to last segment.
        Then moving the second to last segment in self.segments to the position of the segment that is third from last.
        ....etc...
        Then moving the second segment in self.segments to the position of the first segment.
        Finally, it moves first segment in the list forward by DEFAULT_SEGMENT SIZE.

        Where:
        'speed' = user defined input 0 - 10.
        """
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].position())
        self.segments[0].forward(DEFAULT_SEGMENT_SIZE)

    def move_up(self):
        """
        Method that gets the snake travelling upwards on screen.

        It does so by checking 'self.segments[0].heading()'.
        If 'self.segments[0].heading()' is anything except 'DOWN' 'self.segments[0].setheading()' is set to 'UP'.
        """
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        """
       Method that gets the snake travelling downwards on screen.

       It does so by checking 'self.segments[0].heading()'.
       If 'self.segments[0].heading()' is anything except 'UP' 'self.segments[0].setheading()' is set to 'DOWN'.
       """
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        """
       Method that gets the snake travelling left on screen.

       It does so by checking 'self.segments[0].heading()'.
       If 'self.segments[0].heading()' is anything except 'RIGHT' 'self.segments[0].setheading()' is set to 'LEFT'.
       """
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        """
       Method that gets the snake travelling right on screen.

       It does so by checking 'self.segments[0].heading()'.
       If 'self.segments[0].heading()' is anything except 'LEFT' 'self.segments[0].setheading()' is set to 'RIGHT'.
       """
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def extend(self, segment_number):
        """
        Adds 'segment_number' Turtle object segments to end of the snake body.

        It does so by looping through the following procedure 'segment_number' of times.
        It obtains the 'position' of the last segment in 'self.segments'.
        Creates a new invisible Turtle object called segment.
        Sends the new 'segment' to 'position'.
        Assigns the same attributes to the newly created segment as the rest of the objects in 'self.segments'.
        Appends the new segment to the end of the 'self.segments' list.
        Once the segment is appended to 'self.segment' the segment is made visible.
        Where 'segment_number' is a user defined integer 1 - 10.
        """
        for n in range(segment_number):
            x_pos, y_pos = self.segments[-1].position()
            segment = Turtle()
            segment.hideturtle()
            segment.penup()
            if n % 2 == 0:
                segment.color(DARK_GREEN)
            else:
                segment.color(LIGHT_GREEN)
            segment.shape("square")
            segment.turtlesize(SNAKE_GROWTH_FACTOR)
            segment.goto(x_pos, y_pos)
            self.segments.append(segment)
            segment.showturtle()



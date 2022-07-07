"""
A clone of the Hungry Snake Game using OOP.
"""

# Imports.
from time import sleep
from turtle import Screen
from pygame import mixer
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Functions.
def play_game():
    """
    Asks player if they want to play Hungry Snake.
    Returns True if 'yes'.
    Returns False if 'no'.
    """
    while True:
        if games_played < 1:
            play = screen.textinput("Want to play Hungry Snake?", "Type 'Yes' or 'No': ")
            if play.lower() == 'yes':
                return True
            elif play.lower() == 'no':
                return False
        else:
            play = screen.textinput("Want to play again?", "Type 'Yes' or 'No': ")
            if play.lower() == 'yes':
                return True
            elif play.lower() == 'no':
                return False


def food_collision():
    """
    Checks if 'snake.segments[0]' is less than 10 away from 'food.position()'.
    Returns True if condition met.
    """
    if snake.segments[0].distance(food.position()) <= 10:
        return True


def body_collision():
    """
    Checks to see if 'snake.segments[0]' has hit its own body.

    Loops through the segment objects in 'snake.segments' from index[1] to end of list.
    Takes the position of each segment and checks if snake.segments[0] is at distance within 10 of that position.
    Returns True if condition is met.
    """
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment.position()) < 10:
            return True


# Instantiate Screen object.
screen = Screen()

# Setup Screen Parameters.
screen.setup(width=760, height=760)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)

# Initialise mixer.
mixer.init()

# Create counter for games played.
games_played = 0

# Instantiate Scoreboard object.
scoreboard = Scoreboard()

# Start a while loop for 'game_start'.
game_start = play_game()
while game_start:

    # Play background music.
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Create a sound object for eaten food and collisions.
    food_eaten = mixer.Sound("eaten_food.wav")
    collision_occurred = mixer.Sound("crash.wav")

    # Set game variables.
    score = 0
    number_segments = 2     # Number of segments by which to extend snake when food collision occurs.
    level_up = 5            # Number of food items after which to double the 'number_segments'.
    multiplier = 2          # Number by which to multiply 'number_segments' every 'level_up'
    sleep_delay = 0.1      # Starting sleep delay with which to start the game.
    sleep_multiplier = 0.98   # Number by which to multiply the time delay to speed up the game.

    # Instantiate a snake and food object.
    snake = Snake()
    food = Food()

    # Add 1 game to 'games_played'.
    games_played += 1

    # Start listening for key presses.
    screen.listen()
    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.move_left, "Left")
    screen.onkeypress(snake.move_right, "Right")

    # Call spawn() method for snake and food objects. Call create() method for scoreboard object.
    snake.spawn()
    food.spawn()
    scoreboard.create((0, 350), score, "Current Score")

    # Time controller.
    sleep(sleep_delay)

    # Start a while loop for 'game_over'.
    game_over = False
    while not game_over:

        # Set screen.update() and sleep() time delay.
        screen.update()
        sleep(sleep_delay)

        # Call the move() method on the snake object.
        snake.move()

        # Check out of bounds on x-axis.
        if snake.segments[0].xcor() <= -380:
            x_pos, y_pos = snake.segments[0].position()
            snake.segments[0].goto((x_pos + 20) * -1, y_pos)
        if snake.segments[0].xcor() >= 380:
            x_pos, y_pos = snake.segments[0].position()
            snake.segments[0].goto((x_pos - 20) * -1, y_pos)

        # Check out of bounds on y-axis.
        if snake.segments[0].ycor() <= -380:
            x_pos, y_pos = snake.segments[0].position()
            snake.segments[0].goto(x_pos, (y_pos + 20) * -1)
        if snake.segments[0].ycor() >= 380:
            x_pos, y_pos = snake.segments[0].position()
            snake.segments[0].goto(x_pos, (y_pos - 20) * -1)

        # Check for food collision and every 'level_up' increase 'number_segments' to extend by 'multiplier'.
        if food_collision():
            food_eaten.play()
            sleep_delay *= sleep_multiplier
            score += 1
            food.spawn()
            snake.extend(number_segments)
            scoreboard.clear()
            scoreboard.create((0, 350), score, "Current Score")
            if score % level_up == 0:
                number_segments *= multiplier

        # Check for body collision and provide feedback.
        if body_collision():
            collision_occurred.play()
            scoreboard.clear()
            scoreboard.create((0, 0), score, "Try not to eat yourself!\nGAME OVER\nFinal Score")
            game_over = True
            game_start = play_game()
            screen.resetscreen()
            break

# Close game_start while loop with feedback.
scoreboard.clear()
scoreboard.game_over((0, 0))
screen.exitonclick()

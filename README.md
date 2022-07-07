# 100 Days of Python Code

## Project 21: Hungry Snake Game (OOP)

Make a clone of the old 'Hungry Snake' game that used to be on Nokia phones.
Where the snake must eat the randomly generated food items and its size increases with every eaten item.

There are two folders in this repository each with a slightly different version of the snake game. 

The **no_walls** folder hosts a version of the snake game where if the snake moves beyond the boundary of the game screen, 
it will reappear at the same position on the opposite side of the game screen. In this instance of the game,
the aim is to eat all the food without running into your own tail. 

The **walls_kill** folder hosts a version where the snake cannot go beyond the game screen boundaries.
In this instance the aim of the game is to eat all the food without running into a wall or your own tail.

### Controls
The snake is controlled using the up, down, left, and right arrow keys.

### Notes

In booth instances the game can be made easier or harder by modifying some variables 
in the respective main.py files. 

Ones to consider are: 

* `number_segments`: Number of segments by which to extend snake when food collision occurs.
* `level_up`: Number of consecutive food items that need to be eaten for the `multiplier` to be applied to `number segments`.
* `multiplier`: Number by which to multiply 'number_segments' every 'level_up'
* `sleep_delay`: Starting sleep() value for the game time.
* `sleep_multiplier`: Number by which to multiply the time delay after ever eaten food item. 

Run main.py from the respective folder to play game.


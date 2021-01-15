import time
import numpy as np


def process_instructions(instructions: list) -> int:
    # Processes instructions:
    #  'NESW' directions move the ship
    #  'F' moves forward
    #  'L/R' turn the ship
    # Returns: Manhattan distance from start

    directions = ['N', 'E']
    neg_directions = ['S', 'W']
    distances = np.array([0, 0])

    # N/S, E/W
    curr_direction = np.array([0, 1])
    for action, value in instructions:
        if action in directions:
            distances[directions.index(action)] += value
        elif action in neg_directions:
            distances[neg_directions.index(action)] -= value

        elif action == 'F':
            distances += value*curr_direction

        else:
            if action == 'L':
                curr_direction = rotate_vector(curr_direction, value)
            else:
                curr_direction = rotate_vector(curr_direction, -value)

    return abs(distances[0]) + abs(distances[1])


def process_instructions_waypoint(instructions: list) -> int:
    # Processes instructions:
    #  'NESW' directions move the waypoint
    #  'F' moves the ship to the waypoint some number of times in series
    #  'L/R' rotate the waypoint
    # Returns: Manhattan distance from start

    directions = ['N', 'E']
    neg_directions = ['S', 'W']
    distances = np.array([0, 0])

    # N/S, E/W
    curr_direction = np.array([1, 10])
    for action, value in instructions:
        if action in directions:
            curr_direction[directions.index(action)] += value
        elif action in neg_directions:
            curr_direction[neg_directions.index(action)] -= value

        elif action == 'F':
            distances += value*curr_direction

        else:
            if action == 'L':
                curr_direction = rotate_vector(curr_direction, value)
            else:
                curr_direction = rotate_vector(curr_direction, -value)

    return abs(distances[0]) + abs(distances[1])


def rotate_vector(vector: np.ndarray, angle: int) -> np.ndarray:
    # Rotates vector around origin by angle
    # Returns: updated vector

    y = vector[0]
    x = vector[1]

    radius = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    theta += (angle * np.pi/180)

    vector[0] = int(round(radius * np.sin(theta)))
    vector[1] = int(round(radius * np.cos(theta)))

    return vector


start = time.time()

instructions = []
with open('12_input.txt') as f:
    for line in f.readlines():
        instructions.append((line[0], int(line[1:])))

print('Part 1: ', process_instructions(instructions))
# 1533

print('Part 2: ', process_instructions_waypoint(instructions))
# 25235

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 12: Rain Risk ---

Summary:
The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring
at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the
     direction the ship is currently facing.

The ship starts by facing east.

Figure out where the navigation instructions lead. What is the Manhattan
distance between that location and the ship's starting position?

--- Part Two ---

Before you can give the destination to the captain, you realize that the
actual action meanings were printed on the back of the instructions the whole
time. Almost all of the actions indicate how to move a waypoint which is
relative to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-
     clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise)
     the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to
     the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The
waypoint is relative to the ship; that is, if the ship moves, the waypoint
moves with it.

Figure out where the navigation instructions actually lead. What is the
Manhattan distance between that location and the ship's starting position?
"""

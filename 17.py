import time


def update_4d(z, w, x, y, active_cubes: set) -> tuple:
    # Returns (z, w, x, y) if this coordinate
    # remains active based on its neighbors
    # and (-1, -1) otherwise

    neighbors = 0
    for k in [z-1, z, z+1]:
        for h in [w-1, w, w+1]:
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    if (k, h, i, j) in active_cubes:
                        if z == 0 and k == z+1:
                            # Double count when z == 0 bc we only consider +z
                            # and need to count neighbors from z == -1
                            # which is reflection of z == 1
                            neighbors += 2
                        else:
                            neighbors += 1

    if (z, w, x, y) in active_cubes:
        # [3, 4] because we also count the current active cube
        if neighbors in [3, 4]:
            return (z, w, x, y)
    else:
        # 3 because the current cube in inactive
        if neighbors == 3:
            return (z, w, x, y)

    return (-1, -1)


def count(cubes: set) -> int:
    # Returns the number of cubes in a set
    # Because of reflection about z = 0,
    # We count each cube with z > 0 twice

    active_cube_count = 0
    for i in cubes:
        if i[0] == -1:
            continue
        elif i[0] == 0:
            active_cube_count += 1
        else:
            active_cube_count += 2

    return active_cube_count


start = time.time()

"""
Notes: +/- z-coordinates will always be identical
But, when updating z=0, need to double count neighbors with z=1
The 3-D case is the same as the 4-D case with w=0
"""

z0 = []
with open('17_input.txt') as f:
    for line in f.readlines():
        z0.append(list(line.rstrip()))

active_cubes = set()
for i in range(len(z0)):
    for j in range(len(z0)):
        if z0[i][j] == '#':
            active_cubes.add((0, 0, i, j))

for a in range(1, 7, 1):  # 6 cycles
    old_active_cubes = active_cubes.copy()
    active_cubes = set()
    for z in range(0, a+1, 1):  # Consider only pos z bc reflection
        for x in range(-a, len(z0)+a, 1):
            for y in range(-a, len(z0)+a, 1):
                # 3-D case is 4-D case with w = 0
                active_cubes.add(update_4d(z, 0, x, y, old_active_cubes))

print('Part 1: ', count(active_cubes))
# 324

active_cubes = set()
for i in range(len(z0)):
    for j in range(len(z0)):
        if z0[i][j] == '#':
            active_cubes.add((0, 0, i, j))

for a in range(1, 7, 1):  # 6 cycles
    old_active_cubes = active_cubes.copy()
    active_cubes = set()
    for z in range(0, a+1, 1):  # Consider only pos z bc reflection
        for w in range(-a-1, a+1, 1):
            for x in range(-a, len(z0)+a, 1):
                for y in range(-a, len(z0)+a, 1):
                    active_cubes.add(update_4d(z, w, x, y, old_active_cubes))

print('Part 2: ', count(active_cubes))
# 1836

end = time.time()
print('Time elapsed: ', end-start)
# <2s

"""
--- Day 17: Conway Cubes ---

Summary:
[Conway's game of life in higher dimensions]-ish

The pocket dimension contains an infinite 3-dimensional grid. At every integer
coordinate (x,y,z), there exists a single cube which is either active or
inactive. In the initial state of the pocket dimension, almost all cubes start
inactive. The only exception to this is a small flat region of cubes (input);
the cubes start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where
any of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at
x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state
according to the following rules:
    If a cube is active and exactly 2 or 3 of its neighbors are also active,
      the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube
      becomes active. Otherwise, the cube remains inactive.

Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?

--- Part Two ---

For some reason, your simulated results don't match what the experimental
energy source engineers expected. Apparently, the pocket dimension actually
has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer
4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a
hypercube) which is still either active or inactive.

Starting with your initial configuration, simulate six cycles in 4-D space.
How many cubes are left in the active state after the sixth cycle?
"""

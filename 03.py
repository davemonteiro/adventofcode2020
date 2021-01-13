import time


start = time.time()

tree_grid = []
with open('03_input.txt') as f:
    for line in f.readlines():
        tree_grid.append(line.rstrip())

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = []
for slope in slopes:
    tree_count = 0
    col, row = 0, 0

    while row < len(tree_grid):
        if col >= len(tree_grid[0]):
            col -= len(tree_grid[0])

        if tree_grid[row][col] == '#':
            tree_count += 1

        col += slope[0]
        row += slope[1]

    tree_counts.append(tree_count)

print('Part 1: ', tree_counts[1])
# 223

tree_count_product = 1
for tree_count in tree_counts:
    tree_count_product *= tree_count

print('Part 2: ', tree_count_product)
# 3517401300

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport.
While travel by toboggan might be easy, it's certainly not safe: there's very
minimal steering and the area is covered in trees. You'll need to see which
angles will take you near the fewest trees. Due to the local geology, trees in
this area only grow on exact integer coordinates in a grid. You make a map
(your puzzle input) of the open squares (.) and trees (#) you can see.

For example:
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once
involving arboreal genetics and biome stability, the same pattern repeats
to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the
bottom (below the bottom-most row on your map).

Starting at the top-left corner of your map and following a slope of
right 3 and down 1, how many trees would you encounter?

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of
a sudden arboreal stop, after all. Determine the number of trees you would
encounter if, for each of the following slopes, you start at the top-left
corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

What do you get if you multiply together the number of trees
encountered on each of the listed slopes?
"""

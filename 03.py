###
# --- Day 3: Toboggan Trajectory ---
#
# Part 1: Given an infinitely wide but finitely tall grid of empty spaces and trees, return how many trees are crossed traversing the grid starting at 0,0 with a given slope
#
# Part 2: Given an infinitely wide but finitely tall grid of empty spaces and trees, return the product of how many trees are crossed traversing the grid starting at 0,0 given five different slopes
#
###

import time
start = time.time()

tree_grid = []
with open('03_input.txt') as f:
    for line in f.readlines():
        tree_grid.append(line.rstrip())

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
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
#223

tree_count_product = 1
for tree_count in tree_counts:
    tree_count_product *= tree_count

print('Part 2: ', tree_count_product)
#3517401300

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
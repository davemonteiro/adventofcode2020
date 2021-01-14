import time


def step_forward(seat_map: list, neighbor_seats: list) -> list:
    # Returns: Modified list of occupied/empty seats
    #  Similar in spirit to Conway's game of life
    #  Rules in the problem statement

    updated_seats = []
    for row in range(0, len(seat_map)):
        curr_row = []
        for col in range(0, len(seat_map[0])):
            if seat_map[row][col] == 'L':
                occupied_adjacent = 0
                for i, j in neighbor_seats[row][col]:
                    if seat_map[i][j] == '#':
                        occupied_adjacent += 1

                if occupied_adjacent == 0:
                    curr_row.append('#')
                else:
                    curr_row.append('L')

            elif seat_map[row][col] == '#':
                occupied_adjacent = 0
                for i, j in neighbor_seats[row][col]:
                    if seat_map[i][j] == '#':
                        occupied_adjacent += 1

                if occupied_adjacent >= 5:
                    curr_row.append('L')
                else:
                    curr_row.append('#')

            else:
                curr_row.append('.')

        updated_seats.append(curr_row)

    return updated_seats


def fill_seats(seat_map: list, neighbor_seats: list) -> int:
    # Returns: number of occupied seats in final position
    #  Final position is when occupancy doesn't
    #  change between iterations
    occupied_seats = 0
    while True:
        seat_map = step_forward(seat_map, neighbor_seats)

        curr_occupied = sum([row.count('#') for row in seat_map])
        if occupied_seats == curr_occupied:
            return occupied_seats
        else:
            occupied_seats = curr_occupied


start = time.time()

seats = []
with open('11_input.txt') as f:
    for line in f.readlines():
        seats.append([char for char in line.rstrip()])

# Adjacent neighbors
adj_neighbors = []
for row in range(0, len(seats)):
    curr_row = []
    for col in range(0, len(seats[0])):
        curr_neighbors = []
        for i in [row-1, row, row+1]:
            for j in [col-1, col, col+1]:
                if 0 <= i < len(seats) and 0 <= j < len(seats[0]):
                    curr_neighbors.append((i, j))
        curr_row.append(curr_neighbors)
    adj_neighbors.append(curr_row)

# Line of sight neighbors
los_neighbors = []
for row in range(0, len(seats)):
    curr_row = []
    for col in range(0, len(seats[0])):
        curr_neighbors = []

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for i, j in directions:
            curr_i = row + i
            curr_j = col + j
            while 0 <= curr_i < len(seats) and 0 <= curr_j < len(seats[0]):
                if seats[curr_i][curr_j] != '.':
                    curr_neighbors.append((curr_i, curr_j))
                    break
                else:
                    curr_i += i
                    curr_j += j

        curr_row.append(curr_neighbors)
    los_neighbors.append(curr_row)

print('Part 1: ', fill_seats(seats, adj_neighbors))
# 2324

print('Part 2: ', fill_seats(seats, los_neighbors))
# 2068

end = time.time()
print('Time elapsed: ', end-start)
# <2.0s

"""
--- Day 11: Seating System ---

Summary:
By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You
make a quick map of the seat layout (your puzzle input). The seat layout fits
neatly on a grid. Each position is either floor (.), an empty seat (L), or an
occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

All decisions are based on the number of occupied seats adjacent to a
given seat (one of the eight positions immediately up, down, left, right, or
diagonal from the seat). The following rules are applied:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the
        seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also
        occupied, the seat becomes empty.
    Floor (.) never changes; seats don't move, and nobody sits on the floor.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?

--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just
care about adjacent seats - they care about the first seat they can see in each
of those eight directions! Now, instead of considering just the eight
immediately adjacent seats, consider the first seat in each of those eight
directions.

Also, people seem to be more tolerant than you expected: it now takes five or
more visible occupied seats for an occupied seat to become empty (rather than
four or more from the previous rules). The other rules still apply.

Given the new visibility method and the rule change for occupied seats
becoming empty, once equilibrium is reached, how many seats end up occupied?
"""

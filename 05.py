import time


start = time.time()

seat_ids = []
with open('05_input.txt') as f:
    for line in f.readlines():
        row = line[0:7]
        column = line[7:10]

        # Encode seat positions in binary
        row = row.replace('F', '0').replace('B', '1')
        row = int(row, base=2) * 8

        column = column.replace('L', '0').replace('R', '1')
        column = int(column, base=2)

        seat_ids.append(row + column)

print('Part 1: ', max(seat_ids))
# 842

# Locate empty seat = missing integer in [seat_ids]
my_seat = -1
for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids:
        my_seat = i
        break

print('Part 2: ', my_seat)
# 617

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 5: Binary Boarding ---

Summary:
You board your plane only to discover a new problem: you dropped your boarding
pass! You aren't sure which seat is yours, and all of the flight attendants are
busy with the flood of people that suddenly made it through passport control.
Instead of zones or groups, this airline uses binary space partitioning to seat
people. A seat might be specified like FBFBBFFRLR, where F means "front", B
means "back", L means "left", and R means "right". The first 7 characters will
either be F or B; these specify exactly one of the 128 rows on the plane
(numbered 0 through 127). Each letter tells you which half of a region the
given seat is in. Start with the whole list of rows; the first letter
indicates whether the seat is in the front (0 through 63) or the back
(64 through 127). The next letter indicates which half of that region the seat
is in, and so on until you're left with exactly one row.

The last three characters will be either L or R; these specify exactly one of
the 8 columns of seats on the plane (numbered 0 through 7). The same process
as above proceeds again, this time with only three steps.

Every seat also has a unique seat ID: multiply the row by 8, then add the
column. As a sanity check, look through your list of boarding passes.
What is the highest seat ID on a boarding pass?

--- Part Two ---

Time to find your seat. It's a completely full flight, so your seat should
be the only missing boarding pass in your list. However, there's a catch: some
of the seats at the very front and back of the plane don't exist on this
aircraft, so they'll be missing from your list as well. Your seat wasn't at
the very front or back, though; the seats with IDs +1 and -1 from yours will
be in your list.

What is the ID of your seat?
"""

###
# --- Day 5: Binary Boarding ---
#
# Part 1: Given a list of letters that encode binary numbers, find the largest binary number encoded
#
# Part 2: Given a list of ..., return the sole missing number from the middle of the list
#
###

import time
start = time.time()

seat_ids = []
with open('05_input.txt') as f:
    for line in f.readlines():
        row = line[0:7]
        column = line[7:10]

        row = row.replace('F', '0')
        row = row.replace('B', '1')
        row = int(row, base = 2) * 8
        
        column = column.replace('L', '0')
        column = column.replace('R', '1')
        column = int(column, base = 2)

        seat_ids.append(row + column)

print('Part 1: ', max(seat_ids))
#842

seat_ids = sorted(seat_ids)

my_seat = 0
for i in range(1, len(seat_ids) - 2):
    if not seat_ids[i] == (seat_ids[i-1] + 1):
            my_seat = seat_ids[i-1] + 1
            break

print('Part 2: ', my_seat)
#617

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
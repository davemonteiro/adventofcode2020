import time


start = time.time()

earliest_time = -1
bus_IDs = []
with open('13_input.txt') as f:
    earliest_time = int(f.readline().rstrip())
    bus_IDs = f.readline().rstrip().split(',')


smallest_wait = 1000000
winning_ID = -1

for bus in bus_IDs:
    if bus == 'x':
        continue

    temp = earliest_time
    while temp % int(bus) > 0:
        temp += 1

    if (temp - earliest_time) < smallest_wait:
        smallest_wait = (temp - earliest_time)
        winning_ID = int(bus)

print('Part 1: ', smallest_wait * winning_ID)
# 3606

positions = []
simplified_busIDs = []

for bus in bus_IDs:
    if bus == 'x':
        continue
    else:
        simplified_busIDs.append(int(bus))
        positions.append(bus_IDs.index(bus))

"""
Shift the times so that the largest busID leaves at t == 0.
Note: have to undo shift at the end

Doing so reveals two things about the input data:
1. All the bus ID's given are prime. Thus if 2 buses leave at the
same time t, then t must be a multiple of busID_A*busID_B
2. The departure time offsets is such that they can be all
split into two groups, leaving at t==0 and t==31
"""

shift = positions[simplified_busIDs.index(max(simplified_busIDs))]
positions = [x - shift for x in positions]

# These three loops find times when many buses leave simultaneously
for pos in range(0, len(positions)):
    while positions[pos] < 0:
        positions[pos] += simplified_busIDs[pos]

for pos in range(0, len(positions)):
    while positions[pos] >= simplified_busIDs[pos]:
        positions[pos] -= simplified_busIDs[pos]

for pos in range(0, len(positions)):
    while positions.count(positions[pos]) == 1:
        positions[pos] += simplified_busIDs[pos]

offsets = list(set(positions))
products = [1] * len(offsets)

for pos in range(0, len(positions)):
    products[offsets.index(positions[pos])] *= simplified_busIDs[pos]

i = products[0]
while (i + offsets[1]) % products[1] != 0:
    i += products[0]

print('Part 2: ', i - shift)
# 379786358533423

end = time.time()
print('Time elapsed: ', end-start)
# <1s

"""
--- Day 13: Shuttle Search ---

Summary:
Each bus has an ID number that also indicates how often the
bus leaves for the airport. Bus schedules are defined based on a timestamp
that measures the number of minutes since some fixed reference point in the
past. At timestamp 0, every bus simultaneously departed from the sea port.
The time this loop takes a particular bus is also its ID number: the bus with
ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on.

Your notes (your puzzle input) consist of two lines. The first line is your
estimate of the earliest timestamp you could depart on a bus. The second line
lists the bus IDs that are in service according to the shuttle company; entries
that show x must be out of service, so you decide to ignore them. To save time
once you arrive, your goal is to figure out the earliest bus you can take to
the airport. (There will be exactly one such bus.)

What is the ID of the earliest bus you can take to the airport multiplied by
the number of minutes you'll need to wait for that bus?

--- Part Two ---

The shuttle company is running a contest: one gold coin for anyone that can
find the earliest timestamp such that the first bus ID departs at that time
and each subsequent listed bus ID departs at that subsequent minute. (The
first line in your input is no longer relevant.) An x in the schedule means
there are no constraints on what bus IDs must depart at that time.

However, with so many bus IDs in your list, surely the actual earliest
timestamp will be larger than 100000000000000!

What is the earliest timestamp such that all of the listed bus IDs depart at
offsets matching their positions in the list?
"""

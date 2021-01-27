import time


def valid_field(field: int, ranges: list) -> bool:
    # Returns: whether or not an integer (field) is contained
    # within at least one range of integers in a list of ranges
    for r in ranges:
        if field in r:
            return True
    return False


start = time.time()

field_ranges = []
my_ticket = []
other_tickets = []
with open('16_input.txt') as f:
    for line in f.readlines():
        line = line.rstrip().split(' ')
        if len(line) in [4, 5]:
            # Part of the input that provides valid ranges
            first_range = [int(x) for x in line[-3].split('-')]
            second_range = [int(x) for x in line[-1].split('-')]

            valid_values = set()
            for i in list(range(first_range[0], first_range[1]+1)):
                valid_values.add(i)
            for i in list(range(second_range[0], second_range[1]+1)):
                valid_values.add(i)

            field_ranges.append(valid_values)

        if ',' in line[0]:
            line = line[0]

            # First is my ticket
            if len(my_ticket) < 1:
                my_ticket = [int(x) for x in line.split(',')]
            else:
                other_tickets.append([int(x) for x in line.split(',')])

scanning_error_rate = 0
valid_tickets = []
for ticket in other_tickets:
    all_valid = True
    for field in ticket:
        if not valid_field(field, field_ranges):
            all_valid = False
            scanning_error_rate += field

    if all_valid:
        valid_tickets.append(ticket)

print('Part 1: ', scanning_error_rate)
# 28873

# Transpose list of tickets to list of groups of field values
fields = list(map(list, zip(*valid_tickets)))

while any(fields):
    # Once we know what a field is, we set it = 0
    for field in range(len(fields)):
        if fields[field] == 0:
            continue

        results = []
        for r in range(len(field_ranges)):
            results.append(all([f in field_ranges[r] for f in fields[field]]))

        if sum(results) == 1:
            r = results.index(True)
            # The rth field is known, because all of its values
            # are contained only in 1 field_range

            field_ranges[r] = set([field])
            fields[field] = 0

product = 1
for i in field_ranges[0:6]:
    # The first six fields are the 'Departure' fields
    product *= my_ticket[list(i)[0]]

print('Part 2: ', product)
# 2587271823407

end = time.time()
print('Time elapsed: ', end-start)
# <0.1s

"""
--- Day 16: Ticket Translation ---

Summary:
The train ticket you were given is in a language you don't understand.
Unfortunately, you can't actually read the words on the ticket. You can,
however, read the numbers, and so you figure out the fields these tickets must
have and the valid ranges for values in those fields. You collect the rules
for ticket fields, the numbers on your ticket, and the numbers on other nearby
tickets for the same train service (via the airport security cameras) together
into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on
the ticket and the valid ranges of values for each field. For example, a rule
like class: 1-3 or 5-7 means that one of the fields in every ticket is named
class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3
and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

It doesn't matter which position corresponds to which field; you can identify
invalid nearby tickets by considering only whether tickets contain values that
are not valid for any field. In this example, the values on the first nearby
ticket are all valid for at least one field. This is not true of the other
three nearby tickets: the values 4, 55, and 12 are are not valid for any field.
Adding together all of the invalid values produces your ticket scanning error
rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned.
What is your ticket scanning error rate?

--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those
tickets entirely. Use the remaining tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear
on the tickets. The order is consistent between all tickets: if seat is the
third field, it is the third field on every ticket, including your ticket.

Once you work out which field is which, look for the six fields on
your ticket that start with the word departure. What do you get if
you multiply those six values together?
"""

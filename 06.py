###
# --- Day 6: Custom Customs ---
#
# Part 1: Given lists of (lists of strings), find the sum of the count of distinct letters over the lists
#   E.g. List 1 has 4 distinct letters, list 2 has 3... sum = 4+3+...
#
# Part 2: Given lists..., find the sum of the count of letters that appear in all the strings over the lists
#   E.g. List 1 has 4 strings, but only 1 letter appears in each of them ... sum = 1+...
#
###

import time
start = time.time()

group_answers = []
with open('06_input.txt') as f:
    curr_group = {'size' : 0}

    for line in f.readlines():
        if len(line.strip()) == 0:
            # If line is blank, we are finished with a group
            group_answers.append(curr_group)
            curr_group = {'size' : 0}
            
        else:
            curr_group['size'] += 1
            for char in line.rstrip():
                if char in curr_group:
                    curr_group[char] += 1
                else:
                    curr_group[char] = 1

    group_answers.append(curr_group)

print('Part 1: ', sum([(len(x)-1) for x in group_answers]))
#6742


group_letter_counts = []
group_sizes = []

for group in group_answers:
    group_sizes.append(group['size'])
    group_letter_counts.append(list(group.values())[1:])

solution = 0
for group in range(0, len(group_letter_counts)):
    for letter in group_letter_counts[group]:
        if letter == group_sizes[group]:
            solution += 1

print('Part 2: ', solution)
#3447

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
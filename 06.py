import time


start = time.time()

group_answers = []
with open('06_input.txt') as f:
    curr_group = {'size': 0}

    for line in f.readlines():
        if len(line.strip()) == 0:
            # If line is blank, we are finished with a group
            group_answers.append(curr_group)
            curr_group = {'size': 0}

        else:
            curr_group['size'] += 1
            for char in line.rstrip():
                if char in curr_group:
                    curr_group[char] += 1
                else:
                    curr_group[char] = 1

    group_answers.append(curr_group)

print('Part 1: ', sum([(len(x)-1) for x in group_answers]))
# 6742

group_letter_counts = []
group_sizes = []
for group in group_answers:
    group_sizes.append(group['size'])
    group_letter_counts.append(list(group.values())[1:])

solution = 0
for group_idx, group_letters in enumerate(group_letter_counts):
    for letter in group_letters:
        if letter == group_sizes[group_idx]:
            solution += 1

print('Part 2: ', solution)
# 3447

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 6: Custom Customs ---

Summary:
As your flight approaches the regional airport where you'll switch to a much
larger plane, customs declaration forms are distributed to the passengers.
The form asks a series of 26 yes-or-no questions marked a through z. All you
need to do is identify the questions for which anyone in your group answers
"yes". Since your group is just you, this doesn't take very long. However, the
person sitting next to you seems to be experiencing a language barrier and
asks if you can help. For each of the people in their group, you write down
the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

Another group asks for your help, then another, and eventually you've
collected answers from every group on the plane (your puzzle input).

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?

--- Part Two ---

As you finish the last group's customs declaration, you notice that you
misread one word in the instructions: You don't need to identify the questions
to which anyone answered "yes"; you need to identify the questions to
which everyone answered "yes"! Using the same example as above:

For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""

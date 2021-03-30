import time


def sum2(arr: list, total: int) -> int:
    # Returns: the product of two distinct integers in arr that sum to total
    for i_idx, i in enumerate(arr):
        missing_int = total-i
        if missing_int in arr[i_idx+1:]:
            return i*missing_int
    return -1


def sum3(arr: list, total: int) -> int:
    # Returns: the product of three distinct integers in arr that sum to total
    for i_idx, i in enumerate(arr):
        # j comes after i
        for j_idx, j in enumerate(arr[i_idx+1:]):
            missing_int = total-i-j
            # Potential 3rd integer comes after j
            if missing_int in arr[j_idx+1:]:
                return i*j*missing_int
    return -1


start = time.time()

expenses = []
with open('data/01_input.txt') as f:
    for line in f.readlines():
        expenses.append(int(line))

print('Part 1: ', sum2(expenses, 2020))
# 987339

print('Part 2: ', sum3(expenses, 2020))
# 259521570

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 1: Report Repair ---

Summary:
Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.
Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

Find the two entries that sum to 2020;
what do you get if you multiply them together?

--- Part Two ---

In your expense report, what is the product of
the three entries that sum to 2020?
"""

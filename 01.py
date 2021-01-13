import time


def sum2(arr: list, total: int) -> int:
    # Returns: the product of two distinct integers in arr that sum to total
    for i in arr:
        if (total-i) in arr and i != (total-i):
            return i * (total-i)


def sum3(arr: list, total: int) -> int:
    # Returns: the product of three distinct integers in arr that sum to total
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            missing_int = (total - arr[i] - arr[j])
            if missing_int in arr and missing_int not in [arr[i], arr[j]]:
                return (arr[i] * arr[j] * missing_int)


start = time.time()

expenses = []
with open('01_input.txt') as f:
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

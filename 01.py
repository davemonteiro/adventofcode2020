###
# --- Day 1: Report Repair ---
#
# Part 1: Given a list of integers, return the product of the two of them that sum to 2020.
#
# Part 2: Given a list of integers, return the product of the three of them that sum to 2020.
#
###

def sum2(arr: list, total: int) -> int:
    #Returns the product of the two distinct integers in a list that sum to 'total'
    for i in arr:
        if (total - i) in arr:
            return i*(total-i)

def sum3(arr: list, total: int) -> int:
    #Returns the product of the three distinct integers in a list that sum to 'total'
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            missing_int = (total - arr[i] - arr[j])
            if missing_int in arr and arr[i] != missing_int and arr[j] != missing_int:
                return (arr[i] * arr[j] * missing_int)

import time
start = time.time()

expenses = []
with open('01_input.txt') as f:
    for line in f.readlines():
        expenses.append(int(line))

print('Part 1: ', sum2(expenses, 2020))
#987339

print('Part 2: ', sum3(expenses, 2020))
#259521570

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
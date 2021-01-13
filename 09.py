import time


def sum2_in_list(nums: list, total: int) -> bool:
    # Returns: whether or not a list of integers
    #  contains two distinct integers that sum to total

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == total:
                return True
    return False


def find_first_weakness(nums: list, preamble_len: int) -> int:
    # Returns: the first integer in a list for which there are no two integers
    #  in the preceding preamble_len integers that sum to it

    for i in range(preamble_len, len(nums)-1):
        if not sum2_in_list(nums[(i-25):i], nums[i]):
            return nums[i]
    return -1


def find_contiguous_set(nums: list, total: int) -> int:
    # First: finds a set of contiguous integers from a list that sums to total
    # Returns: the sum of the smallest/largest integers within this set

    curr_sum = []
    for i in range(0, len(nums)):
        curr_sum.append(nums[i])
        while sum(curr_sum) > total:
            curr_sum.pop(0)

        if sum(curr_sum) == total:
            return(min(curr_sum) + max(curr_sum))

    return -1


start = time.time()

nums = []
with open('09_input.txt') as f:
    for line in f.readlines():
        nums.append(int(line.rstrip()))

print('Part 1: ', find_first_weakness(nums, 25))
# 1721308972

print('Part 2: ', find_contiguous_set(nums, find_first_weakness(nums, 25)))
# 209694133

end = time.time()
print('Time elapsed: ', end-start)
# <0.05s

"""
--- Day 9: Encoding Error ---

Summary:
With your neighbor happily enjoying their video game, you turn your attention
to an open data port on the little screen in the seat in front of you. Upon
connection, the port outputs a series of numbers (your puzzle input). The data
appears to be encrypted with the eXchange-Masking Addition System (XMAS) which,
conveniently for you, is an old cypher with an important weakness. XMAS starts
by transmitting a preamble of 25 numbers. After that, each number you receive
should be the sum of any two of the 25 immediately previous numbers. The two
numbers will have different values, and there might be more than one such pair.

What is the first number that does not have this property?

--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number
you just found: you must find a contiguous set of at least two numbers in your
list which sum to the invalid number from step 1.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

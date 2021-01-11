###
# --- Day 9: Encoding Error ---
#
# Part 1: Given a list of ints and preamble_len, find the first integer for which
# there are no two ints in the preceding preamble_len integers that sum to it
#
# Part 2: Find a range of integers from the list that sums to the integer found in
# part 1, then return the sum of the smallest and largest ints found in the range 
#
###

def sum2_in_list(nums: list, total: int) -> bool:
    # Returns whether or not a list of integers contains two integers that sum to total
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == total:
                return True
    return False

def find_first_weakness(nums: list, preamble_len: int) -> int:
    # Returns the first integer in a list for which there are no two integers in the 
    # preceding preamble_len integers that sum to it
    for i in range(preamble_len, len(nums) - 1):
        if not sum2_in_list(nums[(i-25):i], nums[i]):
            return nums[i]
    return -1

def find_contiguous_set(nums: list, total: int) -> int:
    # First, finds a contiguous set of integers from a list that sums to a total
    # Returns the sum of the smallest/largest integers within this set
    curr_sum = []
    for i in range(0, len(nums)):
        curr_sum.append(nums[i])
        
        while sum(curr_sum) > total:
            curr_sum.pop(0)
            
        if sum(curr_sum) == total:
            return(min(curr_sum) + max(curr_sum))

    return -1
    
import time
start = time.time()

nums = []
with open('09_input.txt') as f:
    for line in f.readlines():
        nums.append(int(line.rstrip()))
        
print('Part 1: ', find_first_weakness(nums, 25))
#1721308972

print('Part 2: ', find_contiguous_set(nums, 1721308972))
#209694133

end = time.time()
print('Time elapsed: ', end-start)
#<0.02
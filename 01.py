def sum2(arr: list, total: int) -> int:
    #Returns the product of the two distinct integers in arr that sum to total
    for i in arr:
        if (total - i) in arr:
            return i * (total - i)

def sum3(arr: list, total: int) -> int:
    #Returns the product of the three distinct integers in arr that sum to total
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
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

"""
--- Day 1: Report Repair ---

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); 
apparently, something isn't quite adding up. Specifically, they need you to find the two entries that sum to 
2020 and then multiply those two numbers together. For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 
1721 * 299 = 514579, so the correct answer is 514579. Of course, your expense report is much larger. 

Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left 
over from a past vacation. They offer you a second one if you can find three numbers in your expense report
that meet the same criteria. Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
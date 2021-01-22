import time


def memory_game_n_turns(hist: dict, next_num: int, turn: int, n: int) -> int:
    # Returns: nth number spoken

    while turn < n:
        # If seen before
        if next_num in hist:
            temp = next_num
            next_num = (turn - hist[next_num])
            hist[temp] = turn

        # Not seen before
        else:
            hist[next_num] = turn
            next_num = 0

        turn += 1

    return next_num


start = time.time()

numbers = []
with open('15_input.txt') as f:
    numbers = [int(x) for x in f.readline().rstrip().split(',')]

history = {}

turn = 1
next_num = numbers.pop(len(numbers)-1)
for num in numbers:
    if num in history:
        history[num] = turn - history[num]
    else:
        history[num] = turn
    turn += 1

print('Part 1: ', memory_game_n_turns(history.copy(), next_num, turn, 2020))
# 1325

print('Part 2: ', memory_game_n_turns(history, next_num, turn, 30000000))
# 2308180581795

end = time.time()
print('Time elapsed: ', end-start)
# >10s yikes

"""
--- Day 15: Rambunctious Recitation ---

Summary:
In this game, the players take turns saying numbers. They begin by taking
turns reading from a list of starting numbers (your puzzle input). Then,
each turn consists of considering the most recently spoken number:
    If that was the first time the number has been spoken,
        the current player says 0.
    Otherwise, the number had been spoken before; the current player announces
    how many turns apart the number is from when it was previously spoken.

Their question for you is: what will be the 2020th number spoken?

--- Part Two ---

Impressed, the Elves issue you a challenge:
    determine the 30000000th number spoken.
"""

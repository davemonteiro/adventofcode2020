import time


def process_instructions(operations: list, arguments: list) -> int:
    # First: Performs operations on list of arguments
    # Returns: final value of accumulator

    accumulator = 0
    position = 0
    while operations[position] != 'visited':
        if operations[position] == 'nop':
            operations[position] = 'visited'
            position += 1
        elif operations[position] == 'acc':
            accumulator += arguments[position]
            operations[position] = 'visited'
            position += 1
        else:  # == 'jmp'
            operations[position] = 'visited'
            position += arguments[position]

    return accumulator


def process_fixed_instructions(operations: list, arguments: list) -> int:
    # First: "Repairs" list of operations
    # Then: Performs operations on list of arguments
    # Returns: final value of accumulator

    # Locations of jmp or nop instructions
    cands = [pos for pos in range(len(operations)) if operations[pos] != 'acc']
    for i in cands:
        ops = operations[:]
        args = arguments[:]

        if ops[i] == 'jmp':
            ops[i] = 'nop'
        else:
            ops[i] = 'jmp'

        accumulator = 0
        position = 0
        while position < len(ops) and ops[position] != 'visited':
            if ops[position] == 'nop':
                ops[position] = 'visited'
                position += 1
            elif ops[position] == 'acc':
                accumulator += args[position]
                ops[position] = 'visited'
                position += 1
            else:  # == 'jmp'
                ops[position] = 'visited'
                position += args[position]

        if position >= len(ops):
            return accumulator


start = time.time()

operations = []
arguments = []
with open('08_input.txt') as f:
    for line in f.readlines():
        parsed_line = line.rstrip().split(' ')

        operations.append(parsed_line[0])
        arguments.append(int(parsed_line[1]))

print('Part 1: ', process_instructions(operations[:], arguments[:]))
# 1930

print('Part 2: ', process_fixed_instructions(operations, arguments))
# 1688

end = time.time()
print('Time elapsed: ', end-start)
# <0.05s

"""
--- Day 8: Handheld Halting ---

Summary:
Your flight to the major airline hub reaches cruising altitude without
incident. While you consider checking the in-flight menu for one of those
drinks that come with a little umbrella, you are interrupted by the kid
sitting next to you. Their handheld game console won't turn on! They ask if
you can take a look. You narrow the problem down to a strange infinite loop in
the boot code (your puzzle input) of the device. The boot code is represented
as a text file with one instruction per line of text. Each instruction
consists of an operation (acc, jmp, or nop) and an argument
(a signed number like +4 or -20).

    acc increases or decreases a single global value called the accumulator by
        the value given in the argument. After an acc instruction, the
        instruction immediately below it is executed next.
    jmp jumps to a new instruction relative to itself.
    nop stands for No OPeration - it does nothing. The instruction immediately
        below it is executed next.

Immediately before any instruction is executed a second time,
what value is in the accumulator?

--- Part Two ---

After some careful analysis, you believe that exactly one instruction is
corrupted. Somewhere in the program, either a jmp is supposed to be a nop, or
a nop is supposed to be a jmp. (No acc instructions were harmed in the
corruption of this boot code.) The program is supposed to terminate by
attempting to execute an instruction immediately after the last instruction in
the file. By changing exactly one jmp or nop, you can repair the boot
code and make it terminate correctly.

What is the value of the accumulator after the program terminates?
"""

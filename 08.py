###
# --- Day 8: Handheld Halting ---
#
# Part 1: Process a list of instructions in a precise order until you arrive at an instruction previously reached
#
# Part 2: Locate and make the single-instruction modification that fixes the potential infinite loop
#
###

def process_instructions(operations, arguments):
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
        else: #== 'jmp'
            operations[position] = 'visited'
            position += arguments[position]

    return accumulator

def process_fixed_instructions(operations, arguments):
    for i in [pos for pos in range(len(operations)) if operations[pos] != 'acc']:
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
            else: #== 'jmp'
                ops[position] = 'visited'
                position += args[position]

        if position >= len(ops):
            return accumulator

import time
start = time.time()

operations = []
arguments = []
with open('08_input.txt') as f:
    for line in f.readlines():
        parsed_line = line.rstrip().split(' ')

        operations.append(parsed_line[0])
        arguments.append(int(parsed_line[1]))
        
print('Part 1: ', process_instructions(operations[:], arguments[:]))
#1930

print('Part 2: ', process_fixed_instructions(operations, arguments))
#1688

end = time.time()
print('Time elapsed: ', end-start)
#<0.05
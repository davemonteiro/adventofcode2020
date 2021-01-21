import time


def mask_value(mask: str, value: int) -> int:
    # Returns: value after the bitmask is applied

    # Pad value with 0's up to reach 36 digits
    value = str(bin(value))[2:]
    value = (36*'0' + value)[-36:]

    for char in range(0, len(mask)):
        # where bitmask is 0,1 = replace mem address bit with 0,1
        if mask[char] in ['0', '1']:
            value = value[0:char] + mask[char] + value[char+1:]

    return int(value, 2)


def mask_memory(mask: str, mvalue: int) -> list:
    # Returns: list with all memory values that
    # need to be modified after bitmask applied

    # Pad mvalue with 0's up to reach 36 digits
    mvalue = str(bin(mvalue))[2:]
    mvalue = (36*'0' + mvalue)[-36:]

    xs = 0
    for char in range(0, len(mask)):
        # where bitmask is X = floating
        if mask[char] == 'X':
            xs += 1
            mvalue = mvalue[0:char] + 'X' + mvalue[char+1:]

        # where bitmask is 1 = replace mem address bit with 1
        elif mask[char] == '1':
            mvalue = mvalue[0:char] + '1' + mvalue[char+1:]

    memory_locations = []
    for permutation in range(0, 2**xs):
        vals = str(bin(permutation))[2:]
        vals = (36*'0' + vals)[-xs:]

        temp = mvalue
        for val in range(0, xs):
            pos = temp.index('X')
            temp = temp[0:pos] + vals[val] + temp[pos+1:]
        memory_locations.append(temp)

    return memory_locations


start = time.time()

commands = []
with open('14_input.txt') as f:
    for line in f.readlines():
        commands.append(line.rstrip())

mem = {}
current_mask = ''
for command in commands:
    args = command.split(' = ')
    if args[0] == 'mask':
        current_mask = args[1]
    else:
        mem_location = args[0][4:len(args[0])-1]
        mem[mem_location] = mask_value(current_mask, int(args[1]))

print('Part 1: ', sum(mem.values()))
# 11327140210986

mem = {}
current_mask = ''
for command in commands:
    args = command.split(' = ')
    if args[0] == 'mask':
        current_mask = args[1]
    else:
        mem_location = args[0][4:len(args[0])-1]
        for masked_location in mask_memory(current_mask, int(mem_location)):
            mem[masked_location] = int(args[1])

print('Part 2: ', sum(mem.values()))
# 2308180581795

end = time.time()
print('Time elapsed: ', end-start)
# <1s

"""
--- Day 14: Docking Data ---

Summary:
After a brief inspection, you discover that the sea port's computer system
uses a strange bitmask system in its initialization program. Although you
don't have the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask
or write a value to memory. Values and memory addresses are both 36-bit
unsigned integers. For example, ignoring bitmasks for a moment, a line like
mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most
significant bit (representing 2^35) on the left and the least significant
bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied
to values immediately before they are written to memory: a 0 or 1 overwrites
the corresponding bit in the value, while an X leaves the bit in the value
unchanged. For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0

The mask it specifies will overwrite two bits in every written value: the 2s
bit is overwritten with 0, and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By
expanding everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)

To initialize your ferry's docking program, you need the sum of all values
left in memory after the initialization program completes.

What is the sum of all values left in memory after it completes?

--- Part Two ---

For some reason, the sea port's computer system still can't communicate with
your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all.
Instead, it acts as a memory address decoder. Immediately before a value is
written to memory, each bit in the bitmask modifies the corresponding bit of
the destination memory address in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If it is 1, the corresponding memory address bit is overwritten with 1.
    If it is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates
unpredictably. In practice, this means the floating bits will take on all
possible values, potentially causing many memory addresses to be written all
at once!

The entire 36-bit address space still begins initialized to the value 0 at
every address, and you still need the sum of all values left in memory at the
end of the program. In this example, the sum is 208.

What is the sum of all values left in memory after it completes?
"""

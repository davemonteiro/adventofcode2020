import time


def mask_value(mask: str, value: int):
    value = str(bin(value))[2:]
    while len(str(value)) < 36:
        value = '0' + value

    for char in range(0, len(mask)):
        if mask[char] in ['0', '1']:
            value = value[0:char] + mask[char] + value[char+1:]

    return int(value, 2)


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

# print('Part 2: ', )
#

end = time.time()
print('Time elapsed: ', end-start)
# <0.1s

"""
--- Day 14: Docking Data ---

"""

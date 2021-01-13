import time


def bridge_joltage_gap(adapters: int, gap_length: int) -> int:
    # Returns the number of adapter combinations
    # capable of bridging gap_length
    # Gap_length is <= 4
    if gap_length <= 3:
        return 2**(adapters)
    else:
        return (2**(adapters) - 1)


start = time.time()

# Initialize with outlet joltage of 0
joltages = [0]
with open('10_input.txt') as f:
    for line in f.readlines():
        joltages.append(int(line.rstrip()))

# Add final adapter
joltages.append(max(joltages) + 3)

# Use all adapters in ascending order
joltages.sort()

joltage_gaps = [0, 0, 0, 0]
for i in range(0, len(joltages) - 1):
    joltage_gaps[joltages[i+1] - joltages[i]] += 1

print('Part 1: ', joltage_gaps[1]*joltage_gaps[3])
# 2343

# Part 2: because certain adapters are required to be in the final chain,
# we can treat different portions of the chain separately and multiply
# the possible combinations for each section. Each section containing
# optional adapters crosses a joltage gap of <=4, so:
# If the gap is <= 3 jolts, then the adapters are optional (2^n combinations)
# If the gap is 4 jolts, then 1 adapter is required (2^n -1 combinations)

required_adapters = [1]
for i in range(1, len(joltages) - 1):
    if 3 in [(joltages[i] - joltages[i - 1]),
             (joltages[i + 1] - joltages[i])]:
        # If an adjacent adapter joltage differs from the current one
        # by 3, both must be included in the final chain
        required_adapters.append(1)
    else:
        required_adapters.append(0)
required_adapters[len(required_adapters) - 1] = 1

gap_lengths = []
gap_ranges = []
for i in range(0, len(required_adapters) - 1):
    if required_adapters[i] == 0:
        j = i + 1
        while required_adapters[j] == 0:
            j += 1

        gap_lengths.append(j - i)
        gap_ranges.append(joltages[j] - joltages[i - 1])

        while i < j:
            required_adapters[i] = -1
            i += 1

prod = 1
for i in range(0, len(gap_lengths)):
    prod *= bridge_joltage_gap(gap_lengths[i], gap_ranges[i])

print('Part 2: ', prod)
# 31581162962944

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 10: Adapter Array ---

Summary:
The charging outlet near your seat produces the wrong number of jolts. Always
prepared, you make a list of all of the joltage adapters in your bag. Each of
your joltage adapters is rated for a specific output joltage (your puzzle
input). Any given adapter can take an input 1, 2, or 3 jolts lower than its
rating and still produce its rated output joltage. In addition, your device
has a built-in joltage adapter rated for 3 jolts higher than the highest-rated
adapter in your bag.

If you use every adapter in your bag at once, what is the distribution of
joltage differences between the charging outlet, the adapters, and your device?

Find a chain that uses all of your adapters to connect the charging outlet to
your device's built-in adapter and count the joltage differences between the
charging outlet, the adapters, and your device. What is the number of 1-jolt
differences multiplied by the number of 3-jolt differences?

--- Part Two ---

To completely determine whether you have enough adapters, you'll need to
figure out how many different ways they can be arranged. Every arrangement
needs to connect the charging outlet to your device. The previous rules about
when adapters can successfully connect still apply.

You glance back down at your bag and try to remember why you brought so many
adapters; there must be more than a trillion valid ways to arrange them!
Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to
connect the charging outlet to your device?
"""

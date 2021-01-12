def count_valid_outerbag_colors(curr_bag: str, bag_colors: list, bag_contents: list) -> int:
    # Given a bag color, returns the count of possible outer bag colors a bag of this color could be contained within
    
    valid_colors = set()

    contender_bags = [curr_bag]
    while len(contender_bags) > 0:
        active_bag = contender_bags[0]
        for bag in range(0, len(bag_colors)):
            if active_bag in bag_contents[bag]:
                contender_bags.append(bag_colors[bag])
                valid_colors.add(bag_colors[bag])
            
        contender_bags.pop(0)

    return len(valid_colors)

def count_internal_bags(curr_bag: str, bag_colors: list, bag_contents: list) -> int:
    # Given an external bag color, returns the sum of the all the required internal bags, recursively
    pos = bag_colors.index(curr_bag)

    count = 1
    for i in bag_contents[pos].keys():
        if i == 'none':
            continue
        else:
            count += (bag_contents[pos][i] * count_internal_bags(i, bag_colors, bag_contents))

    return count

import time
start = time.time()

bag_colors = []
bag_contents = []
with open('07_input.txt') as f:
    for line in f.readlines():
        parsed_line = line.rstrip().split(' bags contain ')

        bag_colors.append(parsed_line[0])

        contents = parsed_line[1].replace(' bags', '').replace(' bag', '')
        contents = contents.replace(',', '').replace('.', '').split(' ')

        bags = {}
        for i in range(0, len(contents)-2):
            # Every count+two-word color will occupy 3 positions in the list, starting at each i%3==0
            if (i % 3) == 0:
                if contents[i] == 'no':
                    bags['none'] = 0
                else:
                    bags[str(contents[i+1] + ' ' + contents[i+2])] = int(contents[i])

        bag_contents.append(bags)

print('Part 1: ', count_valid_outerbag_colors('shiny gold', bag_colors, bag_contents))
#302

print('Part 2: ', count_internal_bags('shiny gold', bag_colors, bag_contents) - 1)
# Subtract 1 to account for the one bag already owned
#4165

end = time.time()
print('Time elapsed: ', end-start)
#<0.05

"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have
time to grab some food: all flights are currently delayed due to issues in luggage processing. Due to recent
aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags
must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible
for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every
vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on. You have a shiny gold bag. If you
wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag?
(In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
(The list of rules is quite long; make sure you get all of it.)

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of
bags you need to buy! Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags! Of course, the actual rules have a small
chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting
becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""
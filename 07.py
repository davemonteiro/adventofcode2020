import time


def count_valid_outerbag_colors(curr_bag: str,
                                bag_colors: list,
                                bag_contents: list) -> int:
    # Inputs: Color of curr_bag, list of all possible bag colors,
    #  corresponding list of acceptable internal bags for each external bag
    # Returns: Count of unique colored bags curr_bag could be within

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


def count_internal_bags(curr_bag: str,
                        bag_colors: list,
                        bag_contents: list) -> int:
    # Inputs: Color of curr_bag, list of all possible bag colors,
    #  corresponding list of acceptable internal bags for each external bag
    # Returns: Count of bags that could fit within our current bag

    count = 1
    pos = bag_colors.index(curr_bag)
    for i in bag_contents[pos].keys():
        if i == 'none':
            continue
        else:
            count += (bag_contents[pos][i] *
                      count_internal_bags(i, bag_colors, bag_contents))

    return count


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
            # Each count+two-word color occupies 3 values
            # in the list, starting at each i%3==0
            if (i % 3) == 0:
                if contents[i] == 'no':
                    bags['none'] = 0
                else:
                    bags[str(contents[i+1] + ' ' +
                         contents[i+2])] = int(contents[i])

        bag_contents.append(bags)

print('Part 1: ', count_valid_outerbag_colors('shiny gold',
                                              bag_colors,
                                              bag_contents))
# 302

print('Part 2: ', count_internal_bags('shiny gold',
                                      bag_colors,
                                      bag_contents)-1)
# Subtract 1 to account for the one bag already owned
# 4165

end = time.time()
print('Time elapsed: ', end-start)
# <0.05s

"""
--- Day 7: Handy Haversacks ---

Summary:
You land at the regional airport in time for your next flight. In fact, it
looks like you'll even have time to grab some food: all flights are currently
delayed due to issues in luggage processing. Due to recent aviation
regulations, many rules (your puzzle input) are being enforced about bags and
their contents; bags must be color-coded and must contain specific quantities
of other color-coded bags.

How many bag colors can eventually contain at least one shiny gold bag?

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices,
but because of the ridiculous number of bags you need to buy! Consider again
your shiny gold bag.

How many individual bags are required inside your single shiny gold bag?
"""

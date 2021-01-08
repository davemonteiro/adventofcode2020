###
# --- Day 7: Handy Haversacks ---
#
# Part 1: Given a hierarchy of colored bags that must contain specific quantities of other colored bags,
# count the number of bag colors that could eventually contain a bag of the specified color
#
# Part 2: Given a hierarchy of colored bags that must contain specific quantities of other colored bags,
# count the required number of additional bags required to fulfill all bag content requirements
#
###

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
###
# --- Day 7: Handy Haversacks ---
#
# Part 1: 
#
# Part 2: 
#
###

import time
start = time.time()

exterior_bags = []
interior_bags = []
with open('07_input.txt') as f:
    for line in f.readlines():
        parsed_line = line.rstrip().split(' bags contain ')

        exterior_bags.append(parsed_line[0])
        interior_bags.append(parsed_line[1])


valid_colors = set()

contender_bags = ['shiny gold']
while True:
    if len(contender_bags) == 0:
        break
    else:
        active_bag = contender_bags[0]
        for bag in range(0, len(exterior_bags)):
            if active_bag in interior_bags[bag]:
                contender_bags.append(exterior_bags[bag])
                valid_colors.add(exterior_bags[bag])
        
        contender_bags.pop(0)

print('Part 1: ', len(valid_colors))
#302

#print('Part 2: ', solution)
#TBD

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
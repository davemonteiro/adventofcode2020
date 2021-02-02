import time


def combine(lst: list, rules) -> list:
    rule_combinations = []
    if len(lst) == 1:
        return rules[lst[0]]

    elif len(lst) == 2:
        rule_1 = lst[0]
        rule_2 = lst[1]

        for rule1 in rules[rule_1]:
            for rule2 in rules[rule_2]:
                rule_combinations.append(rule1 + rule2)

    elif len(lst) == 3:
        rule_1 = lst[0]
        rule_2 = lst[1]
        rule_3 = lst[2]

        for rule1 in rules[rule_1]:
            for rule2 in rules[rule_2]:
                for rule3 in rules[rule_3]:
                    rule_combinations.append(rule1 + rule2 + rule3)

    else:
        return -1

    return rule_combinations

def combine_pipe(lst1, lst2, rules):
    first_part = combine(lst1, rules)
    second_part = combine(lst2, rules)

    return first_part + second_part


start = time.time()

rules = []
messages = []
with open('19_input.txt') as f:
    for line in f.readlines():
        if ':' in line:
            rules.append(line.rstrip().split(' '))
        else:
            messages.append(line.rstrip())

organized_rules = rules[:]
for rule in rules:
    pos = int(rule[0][:-1])
    organized_rules[pos] = rule[1:]
rules = organized_rules

completed_rules = set()
while len(completed_rules) < len(rules):
    for rule_pos in range(0, len(rules)):
        if rule_pos in completed_rules:
            continue

        rule = rules[rule_pos]
        if len(rule) == 1 and rule[0].isdigit() is False:
            completed_rules.add(rules.index(rule))
            rules[rule_pos] = [str(rule[0][1])]
            continue

        if not set([int(x) for x in rule if x.isdigit()]).issubset(completed_rules):
            # If the current rule requires that other rules be
            # evaluated first, skip the current rule
            continue

        if '|' in rule:
            pos = rule.index('|')
            completed_rules.add(rules.index(rule))
            rules[rule_pos] = combine_pipe(list(map(int, rule[0:pos])), list(map(int, rule[pos+1:])), rules)
            
        elif rule[0].isdigit() is True:
            completed_rules.add(rules.index(rule))
            rules[rule_pos] = combine(list(map(int, rule)), rules)

print('Part 1: ', len([x for x in messages if x in rules[0]]))
# 299

# print('Part 2: ', total_am)
# 65658760783597

end = time.time()
print('Time elapsed: ', end-start)
# >10s !!!

"""

"""

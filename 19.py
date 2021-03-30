import time


def combine_recursive(lst: list, rules: list) -> list:
    message_MAX = 96

    rule_combinations = ['']
    while max([0] + [len(x) for x in rule_combinations]) < message_MAX:
        print('test', max([0] + [len(x) for x in rule_combinations]))

        if len(lst) == 2:
            rule_1 = lst[0]
            rule_2 = rule_combinations[:]

            for rule1 in rules[rule_1]:
                for rule2 in rule_2:
                    rule_combinations.append(rule1 + rule2)

        elif len(lst) == 3:
            rule_1 = lst[0]
            rule_2 = rule_combinations[:]
            rule_3 = lst[2]

            for rule1 in rules[rule_1]:
                for rule2 in rule_2:
                    for rule3 in rules[rule_3]:
                        rule_combinations.append(rule1 + rule2 + rule3)


def combine(lst: list, rules: list) -> list:
    rule_combinations = []
    if len(lst) == 1:
        return rules[lst[0]]

    elif len(lst) == 2:
        rule_1 = lst[0]
        rule_2 = lst[1]

        for rule1 in rules[rule_1]:
            for rule2 in rules[rule_2]:
                rule_combinations.append(rule1 + rule2)

    return rule_combinations


def combine_pipe(lst1, lst2, rule_pos, rules):
    lst1 = list(map(int, lst1))
    lst2 = list(map(int, lst2))

    if rule_pos in lst1 + lst2:
        # Indicates rule contains loop
        return combine_recursive(lst2, rules)
    else:
        first_part = combine(lst1, rules)
        second_part = combine(lst2, rules)
        return first_part + second_part


def process(rules: list) -> set:
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

            prereqs = set([int(x) for x in rule if x.isdigit()])

            if prereqs.issubset(completed_rules):
                # If all prereqs achieved
                if '|' in rule:
                    pos = rule.index('|')
                    completed_rules.add(rules.index(rule))
                    rules[rule_pos] = combine_pipe(rule[0:pos],
                                                   rule[pos+1:],
                                                   rule_pos,
                                                   rules)
                    continue

                else:
                    completed_rules.add(rules.index(rule))
                    rules[rule_pos] = combine(list(map(int, rule)), rules)
                    continue

            prereqs.discard(rule_pos)
            if prereqs.issubset(completed_rules):
                # Only 2 rules of this form, both contain '|'
                pos = rule.index('|')
                completed_rules.add(rules.index(rule))
                rules[rule_pos] = combine_pipe(rule[0:pos],
                                               rule[pos+1:],
                                               rule_pos,
                                               rules)

    rule_zero_options = set(rules[0])
    soln = 0
    for message in messages:
        if message in rule_zero_options:
            soln += 1

    return soln


start = time.time()

rules = []
messages = []

with open('19_input.txt') as f:
    for line in f.readlines():
        if ':' in line:
            rules.append(line.rstrip().split(' '))
        else:
            messages.append(line.rstrip())

# Put rules in ascending order
organized_rules = rules[:]
for rule in rules:
    pos = int(rule[0][:-1])
    organized_rules[pos] = rule[1:]
rules = organized_rules[:]

print('Part 1: ', process(rules))
# 299

organized_rules[8] = ['42', '|', '42', '8']
organized_rules[11] = ['42', '31', '|', '42', '11', '31']

print('Part 2: ', process(organized_rules))
# 65658760783597

end = time.time()
print('Time elapsed: ', end-start)
# >10s !!!

"""

"""

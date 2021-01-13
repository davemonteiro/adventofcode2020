import time


start = time.time()

pw_policies = []
with open('02_input.txt') as f:
    for line in f.readlines():
        pw_policies.append(line.split(' '))

valid_passwords_part1 = 0
valid_passwords_part2 = 0
for pw_policy in pw_policies:
    # Policy is in the form of "a-b X: loremipXsum"

    pw_range = list(map(int, pw_policy[0].split('-')))
    given_letter = pw_policy[1][0]
    pw = pw_policy[2].rstrip()

    # Part 1
    # A password is valid if X occurs in loremipXsum at least
    #  'a' and no more than 'b' times
    instances = pw.count(given_letter)
    if instances >= pw_range[0] and instances <= pw_range[1]:
        valid_passwords_part1 += 1

    # Part 2
    # A password is valid if only one of loremipXsum[a]
    #  and loremipXsum[b] is X
    candidates = []

    if len(pw) >= pw_range[0]:
        candidates.append(pw[pw_range[0]-1])
    if len(pw) >= pw_range[1]:
        candidates.append(pw[pw_range[1]-1])

    if candidates.count(given_letter) == 1:
        valid_passwords_part2 += 1

print('Part 1: ', valid_passwords_part1)
# 600

print('Part 2: ', valid_passwords_part2)
# 245

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 2: Password Philosophy ---

Summary:
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can
take a look. Their password database seems to be a little corrupted: some of
the passwords wouldn't have been allowed by the Official Toboggan Corporate
Policy that was in effect when they were chosen. To try to debug the problem,
they have created a list (your puzzle input) of passwords (according to the
corrupted database) and the corporate policy when that password was set.
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

How many passwords are valid according to their policies?

--- Part Two ---

The shopkeeper suddenly realizes that he just accidentally explained the
password policy rules from his old job at the sled rental place down the
street! The Official Toboggan Corporate Policy actually works a little
differently. Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.

How many passwords are valid according to the
new interpretation of the policies?
"""

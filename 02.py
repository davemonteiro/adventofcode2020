###
# --- Day 2: Password Philosophy ---
#
# Part 1: Given a list of strings, return a count of how many of them contain between 'a' and 'b' instances of a certain letter
#
# Part 2: Given a list of strings, return a count of how many of them contain a certain letter at only one of two given positions
#
###

import time
start = time.time()

valid_passwords_part1 = 0
valid_passwords_part2 = 0
with open('02_input.txt') as f:
    for line in f.readlines():
        # Policy is in the form of "a-b X: loremipXsum"
        password_policy = line.split(' ')
        
        pw_range = list(map(int, password_policy[0].split('-')))
        given_letter = password_policy[1][0]
        pw = password_policy[2].rstrip()
        
        # Part 1
        # A password is valid if X occurs in loremipXsum at least a and no more than b times
        instances = pw.count(given_letter)
        if instances >= pw_range[0] and instances <= pw_range[1]:
            valid_passwords_part1 += 1

        # Part 2
        # A password is valid if only one of loremipXsum[a] and loremipXsum[b] is X
        candidates = []
        
        if len(pw) >= pw_range[0]:
            candidates.append(pw[pw_range[0] - 1])
        if len(pw) >= pw_range[1]:
            candidates.append(pw[pw_range[1] - 1])
        
        if candidates.count(given_letter) == 1:
            valid_passwords_part2 += 1
        
print('Part 1: ', valid_passwords_part1)
#600

print('Part 2: ', valid_passwords_part2)
#245

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
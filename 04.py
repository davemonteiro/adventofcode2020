###
# --- Day 4: Passport Processing ---
#
#Part 1: Given passport data, count the number of 'valid' passports (they contain data for each of 7 (+1 optional) fields)
#
#Part 2: Additional validation criteria: each field's value must follow certain rules 
#
###

def validate_passports(passports: list) -> int:
    # Returns the number of valid passports from a list of passports
    # Validation criteria provided in problem statement
    
    number_valid_passports = 0
    for p in passports:
        # VALIDATE LENGTH
        if len(p) < 8:
            continue

        # VALIDATE DATE FIELDS
        valid_byr = (1920 <= int(p['byr']) <= 2002)
        valid_iyr = (2010 <= int(p['iyr']) <= 2020)
        valid_eyr = (2020 <= int(p['eyr']) <= 2030)

        if not all([valid_byr, valid_iyr, valid_eyr]):
            continue
            
        # VALIDATE HEIGHT
        hgt = p['hgt']
        valid_hgt = True
        while len(hgt) < 4:
            hgt += ' '
 
        val = int(hgt[:-2])
        units = hgt[-2:]
        
        if units == 'cm':
            if not 150 <= val <= 193:
                valid_hgt = False
        elif units == 'in':
            if not 59 <= val <= 76:
                valid_hgt = False
        else:
            valid_hgt = False
            
        if not valid_hgt:
            continue

        # VALIDATE HAIR COLOR
        hcl = p['hcl']
        valid_hcl = True
        if len(hcl) != 7 or hcl[0] != '#':
            valid_hcl = False
    
        for i in hcl[1:]:
            if i not in '0123456789abcdef':
                valid_hcl = False
        
        if not valid_hcl:
            continue
        
        # VALIDATE EYE COLOR
        if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        # VALIDATE PASSPORT ID
        pid = p['pid']
        valid_pid = True

        if len(pid) != 9:
            valid_pid = False

        for i in pid:
            if i not in '0123456789':
                valid_pid = False
        
        if not valid_pid:
            continue

        number_valid_passports += 1
    
    return number_valid_passports

import time
start = time.time()

passports = []
with open('04_input.txt') as f:
    # Initialize passport dict with optional field 'cid' which we anyway ignore
    curr_passport = {'cid':'0'}
    
    for line in f.readlines():
        if len(line.strip()) == 0:
            # If no more fields to be added to the active passport,
            # Add it to the list of completed passports
            # And reinitialize curr_passport
            passports.append(curr_passport)
            curr_passport = {'cid':'0'}
            
        else:
            fields = line.rstrip().split(' ')
            for field in fields:
                curr_passport[field[0:3]] = field[4:]
                
    # Add final passport
    passports.append(curr_passport)

print('Part 1: ', len([p for p in passports if len(p) == 8]))
#208

print('Part 2: ', validate_passports(passports))
#167

end = time.time()
print('Time elapsed: ', end-start)
#<0.01
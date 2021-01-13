import time


def validate_passports(passports: list) -> int:
    # Returns: the number of valid passports from a list of passports
    #  Validation criteria provided in problem statement

    valid_passports = 0
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

        valid_passports += 1

    return valid_passports


start = time.time()

passports = []
with open('04_input.txt') as f:
    # Initialize passport dict with optional field 'cid' which we anyway ignore
    curr_passport = {'cid': '0'}

    for line in f.readlines():
        if len(line.strip()) == 0:
            # If no more fields to be added to the active passport,
            #  add it to the list of completed passports
            #  and reinitialize curr_passport
            passports.append(curr_passport)
            curr_passport = {'cid': '0'}

        else:
            fields = line.rstrip().split(' ')
            for field in fields:
                curr_passport[field[0:3]] = field[4:]

    # Add final passport
    passports.append(curr_passport)

print('Part 1: ', len([p for p in passports if len(p) == 8]))
# 208

print('Part 2: ', validate_passports(passports))
# 167

end = time.time()
print('Time elapsed: ', end-start)
# <0.01s

"""
--- Day 4: Passport Processing ---

Summary:
You arrive at the airport only to realize that you grabbed your North Pole
Credentials instead of your passport. While these documents are extremely
similar, North Pole Credentials aren't issued by a country and therefore aren't
actually valid documentation for travel in most of the world. The automatic
passport scanners are slow because they're having trouble detecting which
passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input).
Passports are separated by blank lines.

Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?

--- Part Two ---

Better add some data validation, quick! You can continue to ignore the cid
field, but each other field has strict rules about what values are valid for
automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present
and valid according to the above rules. Here are some example values:

Count the number of valid passports - those that have all required fields and
valid values. Continue to treat cid as optional.

In your batch file, how many passports are valid?
"""

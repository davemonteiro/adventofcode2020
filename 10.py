###
# --- Day 10: Adapter Array ---
#
# 
#
# 
#
###

def count_paths(nums: list) -> int:
    


import time
start = time.time()

voltages = []
with open('10_input.txt') as f:
    for line in f.readlines():
        voltages.append(int(line.rstrip()))
        

#Add charging outlet voltage
voltages.append(0)

#Final adapter
voltages.append(max(voltages) + 3)

voltages.sort()
counts = [0,0] #1,3
for i in range(0, len(voltages) - 1):
    diff = voltages[i+1] - voltages[i]
    if diff == 1:
        counts[0] += 1
    elif diff == 3:
        counts[1] += 1

print('Part 1: ', counts[0]*counts[1])
#2343





#print('Part 2: ', find_contiguous_set(nums, 1721308972))
#209694133

end = time.time()
print('Time elapsed: ', end-start)
#~0.01
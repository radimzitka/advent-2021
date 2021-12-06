from collections import deque

with open('6.input') as file:
  lines = file.readlines()
  times = lines[0].rstrip().split(',')

lanternfish_ages = 9*[0]

for i in range(len(times)):
    times[i] = int(times[i])
    lanternfish_ages[times[i]] += 1

# Rotate array
lanternfish_ages = deque(lanternfish_ages)

one = True
for i in range(257):
    if(i == 80 or i == 256):
        counter = 0
        for age in lanternfish_ages:
            counter += age
        if(one):
            print("Part one:", counter)
            one = False
        else:
            print("Part two:", counter)
            
    zeros = lanternfish_ages[0]
    lanternfish_ages.rotate(-1)
    lanternfish_ages[6] += zeros

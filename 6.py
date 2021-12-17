from collections import deque

with open('inputs/6.input') as file:
  times = file.readlines()[0].rstrip().split(',')

lanternfish_ages = 9*[0]

for i in range(len(times)):
    lanternfish_ages[int(times[i])] += 1

# Rotate array
lanternfish_ages = deque(lanternfish_ages)

first_task = True
for i in range(257):
    if(i == 80 or i == 256):
        counter = 0
        for age in lanternfish_ages:
            counter += age
        if(first_task):
            print("Part one:", counter)
            first_task = False
        else:
            print("Part two:", counter)
            
    zeros = lanternfish_ages[0]
    lanternfish_ages.rotate(-1)
    lanternfish_ages[6] += zeros

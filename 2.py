with open('inputs/2.input') as file:
  lines = [line.rstrip().split(' ') for line in file.readlines()]

horizontal = 0
depth = 0

aim=0
depth_2 = 0

for line in lines:
    if(line[0] == 'down'):
        depth += int(line[1])
        aim += int(line[1])
    elif(line[0] == 'up'):
        depth -= int(line[1])
        aim -= int(line[1])
    elif(line[0] == 'forward'):
        horizontal += int(line[1])
        depth_2 += int(line[1]) * aim

print("Part one:", horizontal * depth)
print("Part two:", horizontal * depth_2)



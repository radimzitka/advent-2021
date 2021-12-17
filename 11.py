with open('11.input') as file:
  lines = [line.rstrip() for line in file.readlines()]

# Increases all numbers in octopuses
def increase_all(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses)):
            octopuses[y][x] += 1

# Increase all adjacent points
def increase_surroundings(octopuses, x, y, extended_points):
    if(x > 0 and [y, x - 1] not in extended_points):
        octopuses[y][x - 1] += 1

    if(x < len(octopuses) - 1 and [y, x + 1] not in extended_points):
        octopuses[y][x + 1] += 1

    if(y > 0 and [y - 1, x] not in extended_points):
        octopuses[y - 1][x] += 1

    if(y < len(octopuses) - 1 and [y + 1, x] not in extended_points):
        octopuses[y + 1][x] += 1

    if(x > 0 and y > 0 and [y - 1, x - 1] not in extended_points):
        octopuses[y - 1][x - 1] += 1

    if(x > 0 and y < len(octopuses) - 1 and [y + 1, x - 1] not in extended_points):
        octopuses[y + 1][x - 1] += 1

    if(x < len(octopuses) - 1 and y > 0 and [y - 1, x + 1] not in extended_points):
        octopuses[y - 1][x + 1] += 1

    if(x < len(octopuses) - 1 and y < len(octopuses) - 1 and [y + 1, x + 1] not in extended_points):
        octopuses[y + 1][x + 1] += 1

# Make 2D array from input
octopuses = []
for i in range(len(lines)):
    octopuses.append([])
    for j in range(len(lines)):
        octopuses[i].append(int(lines[i][j]))

rounds = 0
flashes = 0
while(True):
    rounds += 1
    extended_points = []

    increase_all(octopuses)

    changed = True

    while(changed):
        changed = False
        for y in range(len(octopuses)):
            for x in range(len(octopuses[y])):
                if(octopuses[y][x] > 9):
                    extended_points.append([y, x])
                    octopuses[y][x] = 0
                    flashes += 1
                    increase_surroundings(octopuses, x, y, extended_points)
                    changed = True
    
    if(rounds == 100):
        print("Part one:", flashes)

    prev = octopuses[0][0]
    all_same = True

    for line in octopuses:
        for number in line:
            if(number != prev):
                all_same = False
                break

        if(all_same == False):
            break
        
    if(all_same == True):
        print("Part one:", rounds)
        break

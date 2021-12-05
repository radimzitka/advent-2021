with open('5.input') as file:
  lines = file.readlines()
  lines = [line.rstrip().split(' -> ') for line in lines]

coord = ""
for i in range(len(lines)):
    lines[i] = [int(lines[i][0].split(',')[0]), int(lines[i][0].split(',')[1]), int(lines[i][1].split(',')[0]), int(lines[i][1].split(',')[1])]

max = 0
for line in lines:
    for number in line:
        if number > max : max = number

coordinates = [[0 for i in range(max + 1)] for j in range(max + 1)]
coordinates_2 = [[0 for i in range(max + 1)] for j in range(max + 1)]

for line in lines:
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    # Swap points if x2 is smaller than x1
    if x2 < x1 : x1, y1, x2, y2 = x2, y2, x1, y1

    # x1 == x2 or y1 == y2
    if(x1 != x2 and y1 != y2 and x2 - x1 != abs(y2 - y1)):
        continue

    # Y coordinate from y2 to y1 (vertical way from up to down)
    if(x1 == x2):
        if(y1 > y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        for c in range(y1, y2 + 1):
            coordinates[x1][c] += 1
            coordinates_2[x1][c] += 1
    
    # X coordinate from x1 to x2 (vertical way from left to right)
    elif(y1 == y2):
        for c in range(x1, x2 + 1):
            coordinates[c][y1] += 1
            coordinates_2[c][y1] += 1
    
    # X is always increasing for next two statements (way right)

    # Y is increasing (way right-down)
    elif(x2 - x1 == y2 - y1):
        y1_temp = y1
        for c in range(x1, x2 + 1):
            coordinates_2[c][y1_temp] += 1
            y1_temp += 1

    # Y is decreasing (way right-up)
    elif(x2 - x1 == y1 - y2):
        y1_temp = y1
        for c in range(x1, x2 + 1):
            coordinates_2[c][y1_temp] += 1
            y1_temp -= 1

# Final counting of every single place in coordinates
counter_1 = counter_2 = 0
for i in range(len(coordinates)):
    for j in range(len(coordinates[i])):
        if(coordinates[i][j] > 1):
            counter_1 += 1
        if(coordinates_2[i][j] > 1):
            counter_2 += 1

print("Part one:", counter_1)
print("Part two:", counter_2)
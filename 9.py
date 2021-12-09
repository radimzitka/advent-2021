with open('9.input') as file:
  lines = [line.rstrip() for line in file.readlines()]

# Count points which are not '9'
def find_neighbours(x, y, arr):
    if(arr[x][y] == '9'):
        return 0
    
    # Point is already counted
    arr[x][y] = '9'

    # Extend about neighbours
    return 1 + find_neighbours(x+1, y, arr) + find_neighbours(x-1, y, arr) + find_neighbours(x, y+1, arr) + find_neighbours(x, y-1, arr)

# Extend basic array about nines at all edges
for i in range(len(lines)):
    lines[i] = '9' + lines[i] + '9'

first_last_row = len(lines[0]) * '9'
lines.insert(0, first_last_row)
lines.append(first_last_row)

counter = 0

# Copy base array due to changes in part two
non_nines = lines[:]
for i in range(len(non_nines)):
    non_nines[i] = list(non_nines[i])

# Array for comparing sizes of clusters
cluster_sizes = 3 * [0]
 
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        # Part one
        height = lines[i][j]
        if(height < lines[i-1][j] and height < lines[i+1][j] and height < lines[i][j-1] and height < lines[i][j+1]):
            counter += int(height) + 1

        # Part two    
        cluster_size = find_neighbours(i, j, non_nines)
        if(cluster_size > cluster_sizes[0]):
            cluster_sizes[0] = cluster_size
            cluster_sizes.sort()

print("Part one:", counter)
print("Part two:", cluster_sizes[0] * cluster_sizes[1] * cluster_sizes[2])

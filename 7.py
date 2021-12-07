with open('7.input') as file:
  lines = file.readlines()
  lines = lines[0].rstrip().split(',')

distances = lines
for i in range(len(distances)):
    distances[i] = int(distances[i])

distances.sort()
# Max item in distances (last item in sort array) for second part
max = distances[len(distances) - 1]

# Middle item
middle = distances[int(len(distances) / 2)]

# First part is only about submiting middle item with others and adding it together
sum = 0
for distance in distances:
    sum += abs(distance - middle)
print("Part one:", sum)

# Array with distances from array for second task (0, 1, 3, 6, 10, ...)
# Counted here because it will be used very often
distance_arr = (max + 1) * [0]
for i in range(1, max + 1):
    distance_arr[i] = distance_arr[i - 1] + i

# Find the cheapest possible outcome 
total_fuel = float("inf")
i = j = middle
while(True):
    sum_fuel_for_i = 0
    sum_fuel_for_j = 0
    for distance in distances:
        sum_fuel_for_i += distance_arr[abs(distance - i)]
        sum_fuel_for_j += distance_arr[abs(distance - j)]

    if(sum_fuel_for_i < total_fuel):
        total_fuel = sum_fuel_for_i
    elif(sum_fuel_for_j < total_fuel):
        total_fuel = sum_fuel_for_i
    else:
        break
    i += 1
    j -= 1

print("Part two:", total_fuel)

